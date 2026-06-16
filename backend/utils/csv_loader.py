import pandas as pd
from pathlib import Path

from backend.database.session import SessionLocal
from backend.models.product import Product


DATA_DIR = Path("data")


def clean_value(value):

    if pd.isna(value):
        return None

    return str(value).strip()


def import_csv(file_path, category):

    print(f"\nImporting {file_path}")

    df = pd.read_csv(file_path)

    db = SessionLocal()

    imported = 0
    skipped = 0

    try:

        unique_products = df.drop_duplicates(
            subset=["Handle"]
        )

        for _, row in unique_products.iterrows():

            handle = clean_value(
                row["Handle"]
            )

            existing = (
                db.query(Product)
                .filter(Product.handle == handle)
                .first()
            )

            if existing:
                skipped += 1
                continue

            product = Product(

                handle=handle,

                title=clean_value(
                    row["Title"]
                ),

                description=clean_value(
                    row["Body (HTML)"]
                ),

                vendor=clean_value(
                    row["Vendor"]
                ),

                product_type=clean_value(
                    row["Type"]
                ),

                tags=clean_value(
                    row["Tags"]
                ),

                category=category,

                published=True,

                image_url=clean_value(
                    row["Image Src"]
                ),

                image_alt_text=clean_value(
                    row["Image Alt Text"]
                ),

                seo_title=clean_value(
                    row["SEO Title"]
                ),

                seo_description=clean_value(
                    row["SEO Description"]
                ),

                google_category=clean_value(
                    row["Google Shopping / Google Product Category"]
                ),

                gender=clean_value(
                    row["Google Shopping / Gender"]
                ),

                age_group=clean_value(
                    row["Google Shopping / Age Group"]
                ),

                condition_type=clean_value(
                    row["Google Shopping / Condition"]
                ),
            )

            db.add(product)

            imported += 1

        db.commit()

        print(
            f"Imported : {imported}"
        )

        print(
            f"Skipped : {skipped}"
        )

    except Exception as e:

        db.rollback()

        print("ERROR:", e)

    finally:

        db.close()


def main():

    import_csv(
        "data/fashion.csv",
        "fashion"
    )

    import_csv(
        "data/jewelry.csv",
        "jewelry"
    )

    import_csv(
        "data/bicycles.csv",
        "bicycle"
    )

    print(
        "\nAll CSV files imported successfully."
    )


if __name__ == "__main__":
    main()