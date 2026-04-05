import pandas as pd

# Load the Excel file with multiple sheets
file_path = "C:\\Users\\AntonisOikonomidis\\Desktop\\data visualisation_2\\datasets visualisation.xlsx" 
#Kindly change the file path. Thank you!

# Step 2: Clean Patients Sheet-------------------------------------------------
patients = pd.read_excel(file_path, sheet_name="patients")

# Convert dates to datetime
patients['screening_date'] = pd.to_datetime(patients['screening_date'], errors='coerce')
patients['randomization_date'] = pd.to_datetime(patients['randomization_date'], errors='coerce')

# Fill missing treatment_group for screen failures
patients['treatment_group'] = patients['treatment_group'].fillna('Screen Failure')

# Flag randomized patients (True if randomized, False if not)
patients['is_randomized'] = patients['randomization_date'].notna()

# Calculate days from screening to randomization (NaN if not randomized)
patients['screen_to_random_days'] = (patients['randomization_date'] - patients['screening_date']).dt.days

# Export cleaned patients sheet
patients.to_csv("clean_patients.csv", index=False)


# Step 3: Clean Sites Sheet----------------------------------------------------

sites = pd.read_excel(file_path, sheet_name="sites")

# Convert site activation date to datetime
sites['site_activation_date'] = pd.to_datetime(sites['site_activation_date'], errors='coerce')

# Optional: make sure target_enrollment is numeric
sites['target_enrollment'] = pd.to_numeric(sites['target_enrollment'], errors='coerce')

# Export cleaned sites sheet
sites.to_csv("clean_sites.csv", index=False)


# Step 4: Clean Adverse Events Sheet-------------------------------------------

adverse_events = pd.read_excel(file_path, sheet_name="adverse_events")

# 1: Convert AE date to datetime
# Robust conversion (handles date, datetime, or text)
adverse_events['ae_date'] = pd.to_datetime(adverse_events['ae_date'], errors='coerce', infer_datetime_format=True)

# Keep only the date (YYYY-MM-DD)
adverse_events['ae_date'] = adverse_events['ae_date'].dt.date


# 2: Standardize serious_ae column

# Ensure Yes/No format and capitalize
adverse_events['serious_ae'] = adverse_events['serious_ae'].str.strip().str.capitalize()

# 3: Add flag for serious AE

# 1 = Serious AE, 0 = Non-serious AE
adverse_events['is_serious'] = adverse_events['serious_ae'].map({'Yes': 1, 'No': 0})

# 4: Export cleaned AE sheet
adverse_events.to_csv("clean_adverse_events.csv", index=False)


# Step 5: Clean Queries Sheet--------------------------------------------------

# Load Queries sheet
queries = pd.read_excel(file_path, sheet_name="queries")


# 1: Convert dates robustly

def to_datetime_safe(col):
    """
    Converts a column to datetime.
    Handles date, datetime, or time-only values.
    Returns pandas datetime64[ns]
    """
    # First, try normal conversion
    dt_col = pd.to_datetime(col, errors='coerce', infer_datetime_format=True)
    
    # If still NaT (e.g., only time), prepend placeholder date
    mask = dt_col.isna()
    if mask.any():
        dt_col[mask] = pd.to_datetime("1900-01-01 " + col[mask].astype(str), errors='coerce')
    return dt_col

queries['querydate'] = to_datetime_safe(queries['querydate'])
queries['last_responsedate'] = to_datetime_safe(queries['last_responsedate'])

# Keep only the date (YYYY-MM-DD)
queries['querydate'] = queries['querydate'].dt.date
queries['last_responsedate'] = queries['last_responsedate'].dt.date


# 2: Calculate days open
# Normal calculation
queries['days_open'] = (pd.to_datetime(queries['last_responsedate']) - pd.to_datetime(queries['querydate'])).dt.days

# If last response missing, use today's date
queries.loc[queries['last_responsedate'].isna(), 'days_open'] = (
    (pd.Timestamp.today().normalize() - pd.to_datetime(queries['querydate'])).dt.days
)


# 3: Standardize query status labels
queries['querystatuslabel'] = queries['querystatuslabel'].str.capitalize()


# 4: Create flags for easy metrics in Power BI
queries['is_open'] = queries['querystatuslabel'].isin(['Raised','Re-raised'])
queries['is_closed'] = queries['querystatuslabel'] == 'Closed'
queries['is_replied'] = queries['querystatuslabel'] == 'Replied'


#5: Export cleaned Queries sheet
queries.to_csv("clean_queries.csv", index=False)

# Optional: preview
print(queries.head())