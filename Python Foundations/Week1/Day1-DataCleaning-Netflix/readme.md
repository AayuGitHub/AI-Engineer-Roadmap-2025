# Day 1 — Netflix Data Cleaning

**Raw file:** data/raw/netflix_titles.csv  
**Processed file:** data/processed/netflix_clean.csv

**Steps performed**
1. Loaded raw CSV and inspected schema / missing values
2. Normalized column names; removed duplicates
3. Parsed date_added and filled missing with release_year fallback
4. Split multi-value fields (cast, country, listed_in) into lists
5. Parsed duration into numeric + unit
6. Normalized rating into categories
7. Saved cleaned CSV and ran basic tests

**Next steps**
- Create feature store or sqlite to store cleaned data
- Build search and filters using cleaned fields