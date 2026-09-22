## Phase 1: Environment Setup & Data Ingestion

Before we start coding, we need a stable environment capable of handling complex geospatial data formats (like GEO TIFFs). GEO TIFFs (Tagged Image File Format) is an image file embedded with geographic metadata to place the image precisely on the Earth's surface. 

**Step 1**: Install Geospatial and ML Dependencies

**Step 2**: Download the sample dataset. LS-SSDD-v1.0 [https://www.kaggle.com/datasets/petrarodriguez/ls-ssdd-v1-0/data?select=JPEGImages_sub_train] is the dataset we're going to use for this project. 

We're done with our first phase after creating a local folder structure, where unprocessed images go under the raw folder, and their bounding box annotations in labels folder. 


## Phase 2: Building the Geospatial Pre-processing Pipeline

SAR images are filled with graininess. This is caused by radar interference. So we'll have to write a script to reduce the graininess. 

**Step 1**: We'll be running the radar noise filter on every image and saving them under the folder processed.

**Step 2**: Converting the dataset's XML (Pascal VOC) annotations into YOLO TXT format. We'll be creating a separate python file by the name convert_labels.ipynb to perform this.

**Step 3**: Run the Automatic Dataset Splitter on both the images folder and labels folder. We create another separate python file named split_dataset.ipynb to perform this. We do this because YOLO needs data strictly separated into train and val sets. 

Once this finishes running, our pipeline's data engineering phase is complete.


## Phase 3: Model Training & Tuning

We'll be using YOLOv8 as it gives a state of the art balance between speed and accuracy. 

**Step 1**: We create a file named dataset.yaml to tell YOLO where to find the data. 

**Step 2**: We initiate the training from pre-trained weights in main.ipynb file

**Step 3**: We look closely at mAP50-95 and the generated confusion matrix. 

<img width="3000" height="2250" alt="confusion_matrix" src="https://github.com/user-attachments/assets/e9fd8c67-ed72-4203-a32d-44325de03255" />

<img width="2400" height="1200" alt="results" src="https://github.com/user-attachments/assets/c88a0e56-267f-4b20-beda-8382bd065f64" />


## Phase 4: Production Packaging 

To ensure our pipeline runs anywhere including Microsoft Azure environments, we create a Dockerfile

**Step 1**: Containerize with Docker by building the container image

**Step 2**: We test the production pipeline container

After passing any validation image into the container, we see a spit out clean, cloud-ready JSON detection coordinates instantly. 
