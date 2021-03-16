# train_ml_gcp
This dir guides you to **create ML models, package models as apps, submit, and log training jobs** on GCP.

## Package structure
![](https://cloud.google.com/ai-platform/images/recommended-project-structure.png)
Look at the above strucutre, remember that
Your ML package should have:
- **setup.py** - script to package your app either automatically by *gcloud* command or manually.
- **trainer** dir - all codes for initializing and training ML models goes here.
- **other_subpackage** dir - all other codes to supplement **trainer**. For example: *upload_to_gcs* script helps to upload trained models to Google Cloud Storage for later deployment
