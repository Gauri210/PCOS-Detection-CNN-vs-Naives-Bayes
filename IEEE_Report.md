# Comparative Analysis of Naive Bayes and Convolutional Neural Networks for Automated PCOS Detection from Ultrasound Imagery

**Author:** Gauri
**Date:** April 2026

---

## Abstract
Polycystic Ovary Syndrome (PCOS) is a common hormonal disorder among women of reproductive age. Early and accurate detection through ultrasound imagery is very important for effective treatment. However, manually interpreting these ultrasound images can be subjective and prone to human error. In this project, we built an automated computer program to classify ovarian ultrasound images into 'Normal' and 'Abnormal' (showing PCOS) categories. We compared two different machine learning methods: a traditional Gaussian Naive Bayes model and a more advanced Convolutional Neural Network (CNN). Both models were trained and tested on a custom dataset of ultrasound images. We evaluated their performance using Accuracy, Precision, Recall, and F1-Score. Our results show that the CNN, which automatically learns spatial patterns in images, significantly outperforms the simpler Naive Bayes model, making it a much more reliable tool for medical diagnosis.

**Keywords:** Polycystic Ovary Syndrome (PCOS), Ultrasound Imaging, Convolutional Neural Networks (CNN), Naive Bayes, Machine Learning, Medical Image Classification.

---

## I. Introduction
Polycystic Ovary Syndrome (PCOS) affects a significant percentage of women globally, often characterized by irregular menstrual cycles, hyperandrogenism, and polycystic ovaries visible on ultrasound. Manual interpretation of ultrasound images by radiologists can be subjective, time-consuming, and prone to human error. Consequently, developing automated, computer-aided diagnosis (CAD) systems using machine learning and computer vision has become a critical area of research.

In this project, we investigate the application of automated image classification techniques to detect structural abnormalities indicative of PCOS in ultrasound scans. We compare two fundamentally different classification methodologies: 
1. **Gaussian Naive Bayes (NB):** A probabilistic classifier that assumes feature independence, applied to flattened image pixels.
2. **Convolutional Neural Network (CNN):** A deep learning architecture designed to automatically learn hierarchical spatial hierarchies of features from images.

The objective is to analyze the performance trade-offs between a computationally lightweight traditional algorithm and a more complex, data-driven deep learning architecture for this specific medical imaging task.

## II. Methodology

### A. Dataset Information
The dataset utilized consists of ultrasound images categorized into two primary classes based on the `abnormality` label:
- **Class 0 (Normal):** Images labeled as 'Appears normal' or 'Not-visible'.
- **Class 1 (Abnormal):** Images labeled as 'Appears abnormal' or 'Visible' (indicative of PCOS).

The data is split into a designated training set (`updated train dataset`) containing labeled samples, and a test set (`updated test dataset`) used for blind prediction generation.

![Class Distribution](file:///c:/Users/Gauri/Downloads/IDSA%20Project/graph_cell_4_0.png)
*Figure 1: Class Distribution in the Training Dataset, highlighting the categorical imbalance between Normal and Abnormal (PCOS) morphologies.*

![Training Samples](file:///c:/Users/Gauri/Downloads/IDSA%20Project/graph_cell_6_0.png)
*Figure 2: Sample images from the training dataset showing 'Normal' and 'Abnormal' (PCOS visible) ovaries.*

### B. Image Preprocessing
To ensure consistent input dimensions and reduce computational complexity, all images underwent the following preprocessing pipeline:
1. **Grayscale Conversion:** Images were read in grayscale, as morphological features in ultrasound do not rely heavily on color information.
2. **Resizing:** All images were resized to a fixed resolution of 128 $\times$ 128 pixels.
3. **Normalization:** Pixel intensities were scaled to a range of [0, 1] by dividing by 255.0.

### C. Gaussian Naive Bayes Model
For the Naive Bayes model, the spatial structure of the images was discarded:
1. **Flattening:** The 128 $\times$ 128 images were flattened into 1D arrays of 16,384 features.
2. **Standardization:** The flattened features were normalized using a `StandardScaler` to achieve zero mean and unit variance, a standard requirement for optimizing the performance of many machine learning estimators.

![Structural Difference Heatmap](file:///c:/Users/Gauri/Downloads/IDSA%20Project/graph_cell_10_2.png)
*Figure 3: Visual structural comparison: Average Normal Ultrasound, Average Abnormal (PCOS) Ultrasound, and the resulting Structural Difference Heatmap.*

![Pixel Intensity Distribution](file:///c:/Users/Gauri/Downloads/IDSA%20Project/graph_cell_12_3.png)
*Figure 4: Kernel Density Estimation of Pixel Intensity Distributions across Normal and Abnormal classes. The significant overlap complicates baseline probabilistic classification.*
3. **Modeling:** A Gaussian Naive Bayes (`GaussianNB`) model was trained on the scaled 1D vectors to predict the binary class labels.

### D. Convolutional Neural Network (CNN) Model
To capture spatial dependencies and texture features inherent in ultrasound images, a custom CNN was designed using TensorFlow/Keras. The architecture is as follows:
1. **Convolutional Blocks:** Four sequential blocks, each containing:
   - A 2D Convolutional Layer (`Conv2D`) with $3 \times 3$ kernels, ReLU activation, and 'same' padding. Filter sizes progressively increased (32 $\rightarrow$ 64 $\rightarrow$ 128 $\rightarrow$ 256).
   - A $2 \times 2$ Max Pooling layer to reduce spatial dimensions.
   - Batch Normalization (`BatchNormalization`) to stabilize and accelerate training.
2. **Dense Layers:** 
   - A `Flatten` layer to convert the 2D feature maps to a 1D vector.
   - Two Fully Connected (`Dense`) layers with 256 and 128 units respectively, utilizing ReLU activation.
   - Dropout layers (rate = 0.5) after each Dense layer to mitigate overfitting.
3. **Output Layer:** A `Dense` layer with 2 units and 'softmax' activation for binary classification probabilities.

The CNN was compiled using the Adam optimizer and Sparse Categorical Crossentropy loss. Data augmentation (rotation, width/height shifts, zoom) was applied during training over 50 epochs with an 80-20 validation split to enhance model generalization.

## III. Results and Evaluation

### A. Evaluation Metrics
The models were evaluated using the following standard classification metrics derived from the Confusion Matrix:
- **Accuracy:** The ratio of correctly predicted observations to the total observations.
- **Precision:** The ratio of correctly predicted positive observations to the total predicted positives.
- **Recall (Sensitivity):** The ratio of correctly predicted positive observations to the all observations in actual class.
- **F1-Score:** The weighted average of Precision and Recall.

### B. Model Performance
*(Note: As the project focuses on training data performance comparisons before generating final blind test predictions, the metrics below reflect the models' fitting capabilities on the training distribution.)*

#### 1) Naive Bayes Classifier Results
The Naive Bayes model, relying strictly on independent pixel intensities, serves as a functional baseline.
- **Accuracy:** 61.19%
- **Precision:** 86.20%
- **Recall:** 54.68%
- **F1-Score:** 66.92%

![Naive Bayes Confusion Matrix](file:///c:/Users/Gauri/Downloads/IDSA%20Project/graph_cell_14_1.png)
*Figure 2: Confusion Matrix for the Naive Bayes model on training data.*

#### 2) CNN Training and Results
The CNN, leveraging learned spatial filters, significantly outperforms the baseline. The training process over 50 epochs demonstrated steady convergence, with the architecture effectively managing the variance often seen in limited medical datasets.

![CNN Training Curves](file:///c:/Users/Gauri/Downloads/IDSA%20Project/graph_cell_23_2.png)
*Figure 3: Training and validation accuracy and loss over 50 epochs for the CNN.*

- **Accuracy:** 78.78%
- **Precision:** 77.59%
- **Recall:** 99.04%
- **F1-Score:** 87.01%

![CNN Confusion Matrix](file:///c:/Users/Gauri/Downloads/IDSA%20Project/graph_cell_26_3.png)
*Figure 4: Confusion Matrix for the CNN model on training data.*

#### 3) Performance Comparison
The performance comparison yields a quantifiable difference, demonstrating the CNN's superior capability in distinguishing normal ovarian tissue from abnormal, polycystic patterns. The CNN achieved a massive +17.59% increase in overall accuracy compared to the Naive Bayes baseline, with a remarkably high recall (99.04%) which is critical for medical screening to minimize false negatives.

| Metric | Naive Bayes | CNN |
| --- | --- | --- |
| **Accuracy** | 0.6119 | 0.7878 |
| **Precision** | 0.8620 | 0.7759 |
| **Recall** | 0.5468 | 0.9904 |
| **F1-Score** | 0.6692 | 0.8701 |

![Performance Comparison Chart](file:///c:/Users/Gauri/Downloads/IDSA%20Project/graph_cell_31_4.png)
*Figure 5: Bar chart comparison of evaluation metrics between Naive Bayes and CNN.*

### C. Final Predictions
Following evaluation, both models generated predictions on the unseen test dataset. The results, containing the `image_name`, `naive_bayes_prediction`, and `cnn_prediction`, were exported to `pcod_predictions.csv` for further clinical or operational review.

## IV. Conclusion and Future Work
This study successfully implemented and compared Naive Bayes and Convolutional Neural Networks for the automated detection of PCOS from ultrasound imagery. The results emphasize that while traditional, pixel-wise machine learning models like Naive Bayes can establish a functional baseline, deep learning architectures like CNNs are fundamentally better suited for the complexities of medical image analysis. The spatial hierarchies learned by the CNN provide a more robust and accurate classification mechanism, paving the way for more reliable Computer-Aided Diagnosis tools in gynecology. Future work may involve exploring transfer learning with pre-trained models (e.g., ResNet, VGG) or incorporating attention mechanisms to further isolate critical regions of interest within the ultrasound scans.

## References
1. O. Faust et al., "Deep learning for healthcare applications based on physiological signals: A review," *Computer Methods and Programs in Biomedicine*, 2018.
2. A. Esteva et al., "A guide to deep learning in healthcare," *Nature Medicine*, vol. 25, no. 1, pp. 24-29, 2019.
3. Scikit-learn: Machine Learning in Python, Pedregosa et al., JMLR 12, pp. 2825-2830, 2011.
4. M. Abadi et al., "TensorFlow: Large-scale machine learning on heterogeneous systems," 2015.
