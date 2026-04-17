import pandas as pd
import numpy as np
import re

class DataCleaning:

    def clean_data(self, df):
        print("🔹 Universal Data Cleaning Started...")

        # =========================
        # 1. Remove duplicates
        # =========================
        df = df.drop_duplicates()

        # =========================
        # 2. Standardize column names
        # =========================
        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_", regex=False)
            .str.replace("-", "_", regex=False)
        )

        # =========================
        # 3. Replace invalid values
        # =========================
        df.replace(
            ["", " ", "nan", "none", "null", "NaN", "NULL"],
            np.nan,
            inplace=True
        )

        # =========================
        # 4. Convert numeric columns safely
        # =========================
        for col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='ignore')

        # =========================
        # 5. Detect column types
        # =========================
        num_cols = df.select_dtypes(include=['int64', 'float64']).columns
        text_cols = df.select_dtypes(include=['object']).columns

        # =========================
        # 6. Handle missing values
        # =========================
        for col in num_cols:
            df[col].fillna(df[col].median(), inplace=True)

        for col in text_cols:
            mode_val = df[col].mode()
            df[col].fillna(mode_val[0] if not mode_val.empty else "unknown", inplace=True)

        # =========================
        # 7. Clean text columns
        # =========================
        for col in text_cols:
            df[col] = (
                df[col]
                .astype(str)
                .str.strip()
                .str.lower()
            )

        # =========================
        # 8. Email validation
        # =========================
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        email_cols = [col for col in text_cols if "email" in col]

        for col in email_cols:
            df[col] = df[col].apply(
                lambda x: x if re.match(email_pattern, str(x)) else np.nan
            )

            df[col].fillna("invalid_email", inplace=True)

        # =========================
        # 9. Date conversion (optional smart detection)
        # =========================
        for col in text_cols:
            if "date" in col or "time" in col:
                df[col] = pd.to_datetime(df[col], errors='coerce')

        # =========================
        # 10. Outlier handling (IQR method - SAFE)
        # =========================
        mask = pd.Series(True, index=df.index)

        for col in num_cols:
            if df[col].nunique() > 5:
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1

                lower = Q1 - 1.5 * IQR
                upper = Q3 + 1.5 * IQR

                mask &= df[col].between(lower, upper)

        df = df[mask]

        # =========================
        # 11. Reset index
        # =========================
        df = df.reset_index(drop=True)

        print("✅ Universal Data Cleaning Completed Successfully!")

        return df