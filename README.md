
# **Be My Chef AI - Recipe Generation from Food Images**

![Be My Chef AI Logo](asset/Demo images/be my chef.png) <!-- Replace with the actual path to your logo image -->

Are you curious about recreating delicious dishes from just a picture? **Be My Chef AI** is here to help! This project leverages advanced AI models to generate detailed recipes based on food images. By analyzing a picture of a dish, the system predicts the ingredients and provides step-by-step cooking instructions to recreate it.

<!--## **Demo**

[![Demo Image](asset/Demo images/be my chef.png)](http://localhost:8501) <!-- Replace with a link to your demo video or live app -->
## Project Link

Check out the live version of the project [here](https://be-my-chef-ai.streamlit.app/).


Upload an image, and watch as the AI generates a complete recipe for you!

## **Features**

- **Image-Based Ingredient Prediction**: Upload a food image, and the AI predicts the ingredients present.
- **Recipe Generation**: Generates a detailed recipe with a title, ingredients list, and cooking instructions.
- **Multiple Chef Models**: Choose between different chef personas for varied recipe styles.
- **User-Friendly Interface**: Easy-to-use interface built with Streamlit.

## **Model Details**

The application uses a combination of Convolutional Neural Networks (CNNs) and Transformer models:

- **CNN Encoder**: Processes the input food image to extract visual features.
- **Ingredient Decoder**: Predicts the ingredients present in the dish.
- **Transformer Decoder**: Generates the cooking instructions based on the predicted ingredients and image features.

## **Setup Instructions**

### **1. Prerequisites**

#### a. **Install Conda (if not installed)**

Download and install Miniconda from the [official website](https://docs.conda.io/en/latest/miniconda.html) suitable for your operating system.

#### b. **Download Model Files**

You need to download three essential files for the model to function:

1. **Model Weights**: [Download `modelbest.ckpt`](https://dl.fbaipublicfiles.com/inversecooking/modelbest.ckpt)
2. **Ingredients Vocabulary**: [Download `ingr_vocab.pkl`](https://dl.fbaipublicfiles.com/inversecooking/ingr_vocab.pkl)
3. **Instruction Vocabulary**: [Download `instr_vocab.pkl`](https://dl.fbaipublicfiles.com/inversecooking/instr_vocab.pkl)

Place these files in the `Foodimg2Ing/data/` directory within your project folder.

### **2. Installation**

#### a. **Clone the Repository**

```bash
git clone https://github.com/GaneshAdimalupu/Recipe-Generation-from-Food-Image.git
cd Recipe-Generation-from-Food-Image
```

#### b. **Create and Activate Conda Environment**

```bash
conda create -n ganesh[your Name] python=3.8
conda activate ganesh[your Name]
```

#### c. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3. Running the Application**

Start the Streamlit app by running:

```bash
streamlit run app.py
```

After running this command, you will see output similar to:

```
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.X.XXX:8501
```

Open the Local URL in your web browser to interact with the app.

### **Using the App**

1. **Upload a Food Image**: Click on "Choose a food image" and select an image (jpg, jpeg, or png).
2. **View Uploaded Image**: The app will display the image you've uploaded.
3. **Ingredient Prediction**: The app processes the image and predicts the ingredients.
4. **Select Chef Model**: Choose between "Chef Scheherazade" or "Chef Giovanni" for different recipe styles.
5. **Generate Recipe**: Click on "Get Recipe!" to generate the recipe.
6. **View Recipe**: The app will display the recipe title, ingredients list, and cooking instructions.

## **Screenshots**

<!-- Replace with actual screenshot path -->

## **Project Structure**

```
├── app.py                          # Main application entry point
├── asset                           # Directory for static assets (CSS, images, fonts, etc.)
│   ├── css
│   │   └── style.css               # Main stylesheet for the web app
│   ├── Demo images
│   │   ├── 2.png                   # Sample image for demo purposes
│   │   └── be my chef.png          # Demo image for the "Be My Chef" feature
│   ├── fonts
│   │   ├── Montserrat-Bold.ttf     # Font: Montserrat bold version
│   │   ├── Montserrat-Regular.ttf  # Font: Montserrat regular version
│   │   ├── Poppins-Bold.ttf        # Font: Poppins bold version
│   │   └── Poppins-Medium.ttf      # Font: Poppins medium version
│   ├── frame
│   │   ├── export
│   │   │   └── food-image-logo.png  # Exported food logo image
│   │   ├── food-image-logo-background.png  # Background for food image logo
│   │   ├── food-image-logo-bg-g.png        # Green background version of the food logo
│   │   ├── food-image-logo-bg-s.png        # Silver background version of the food logo
│   │   ├── food.jpg                       # Food image used in the app
│   │   ├── logo.png                       # Logo for the app
│   │   ├── no_food.png                    # Placeholder for when no food is detected
│   │   └── recipe-bg.png                  # Background image for recipe section
│   ├── images
│   │   ├── chef-transformer.png           # Image of chef transformer for UI
│   │   ├── chef-transformer-transparent.png # Transparent version of the chef transformer image
│   │   ├── frames                         # Folder containing various frame images for UI
│   │   │   ├── 10.jpg                     # Frame image 10
│   │   │   ├── 1.jpg                      # Frame image 1
│   │   │   ├── 2.jpg                      # Frame image 2
│   │   │   ├── 3.jpg                      # Frame image 3
│   │   │   ├── 4.jpg                      # Frame image 4
│   │   │   ├── 5.jpg                      # Frame image 5
│   │   │   ├── 6.jpg                      # Frame image 6
│   │   │   ├── 7.jpg                      # Frame image 7
│   │   │   ├── 8.jpg                      # Frame image 8
│   │   │   └── 9.jpg                      # Frame image 9
│   │   ├── logo.png                       # Logo for the app
│   │   ├── recipe-frame.png               # Frame used for displaying recipes
│   │   ├── recipe.jpg                     # Sample recipe image
│   │   └── recipe-post.png                # Image used for posting recipes
│   └── Recipe Gen images                  # Folder for images related to recipe generation
├── chef_transformer                      # Core model-related code
│   ├── CONTRIBUTING.md                   # Guide for contributing to the project
│   ├── dummy.py                          # Dummy file for testing
│   ├── examples.py                       # Example usage of chef_transformer model
│   ├── meta.py                           # Meta information about the model and its setup
│   ├── notes
│   │   └── Build Ingredients Vocab.ipynb # Notebook for building an ingredient vocabulary
│   ├── __pycache__                       # Compiled Python files (autogenerated)
│   │   ├── dummy.cpython-38.pyc          # Cached bytecode of dummy.py
│   │   ├── examples.cpython-38.pyc       # Cached bytecode of examples.py
│   │   └── meta.cpython-38.pyc           # Cached bytecode of meta.py
│   ├── README.md                         # Readme file for understanding the module
│   └── requirements.txt                  # Dependencies required for the chef_transformer module
├── data                                  # Directory for model data files
│   ├── ingr_vocab.pkl                    # Pickled ingredient vocabulary
│   ├── instr_vocab.pkl                   # Pickled instruction vocabulary
│   └── modelbest.ckpt                    # Model checkpoint for best-performing model
├── eval                                  # Evaluation-related scripts and files
│   ├── Chef_Transformer_Evaluation.ipynb # Evaluation notebook for Chef Transformer model
│   ├── ChefTransformer_predicted.json    # JSON file of Chef Transformer model predictions
│   ├── RecipeNLG_Evaluation.ipynb        # Evaluation notebook for RecipeNLG model
│   ├── RecipNLG_predicted.json           # JSON file of RecipeNLG model predictions
│   └── test-5000.csv                     # Test dataset for model evaluation
├── Foodimg2Ing                           # Code for converting food images to ingredients
│   ├── args.py                           # Argument parser for the Foodimg2Ing model
│   ├── __init__.py                       # Init file for module import
│   ├── model.py                          # Model definition for Foodimg2Ing
│   ├── output.py                         # Output processing for Foodimg2Ing results
│   ├── __pycache__                       # Cached bytecode for the module (autogenerated)
│   │   ├── args.cpython-38.pyc           # Cached bytecode of args.py
│   │   ├── __init__.cpython-38.pyc       # Cached bytecode of __init__.py
│   │   ├── model.cpython-38.pyc          # Cached bytecode of model.py
│   │   ├── output.cpython-38.pyc         # Cached bytecode of output.py
│   │   └── routes.cpython-38.pyc         # Cached bytecode of routes.py
│   └── routes.py                         # API routes for processing images to ingredients
├── modules                               # Transformer-related core modules
│   ├── encoder.py                        # Encoder module for the transformer model
│   ├── multihead_attention.py            # Multi-head attention mechanism
│   ├── __pycache__                       # Cached bytecode for modules (autogenerated)
│   │   ├── encoder.cpython-38.pyc        # Cached bytecode of encoder.py
│   │   ├── multihead_attention.cpython-38.pyc # Cached bytecode of multihead_attention.py
│   │   ├── transformer_decoder.cpython-38.pyc # Cached bytecode of transformer_decoder.py
│   │   └── utils.cpython-38.pyc          # Cached bytecode of utils.py
│   ├── transformer_decoder.py            # Transformer decoder module
│   └── utils.py                          # Utility functions for the transformer modules
├── Procfile                              # Process file for deployment (e.g., Heroku)
├── README.md                             # Project description and setup guide
├── requirements.txt                      # Dependencies required for the entire project
└── utils                                 # Miscellaneous utility functions
    ├── api.py                            # API-related utilities
    ├── draw.py                           # Utility for drawing or visualizing data
    ├── ext.py                            # External processing utilities
    ├── ims2file.py                       # Image-to-file conversion utility
    ├── __init__.py                       # Init file for module import
    ├── metrics.py                        # Functions for evaluating model performance
    ├── output_utils.py                   # Utilities for handling output processing
    ├── __pycache__                       # Cached bytecode (autogenerated)
    │   ├── api.cpython-38.pyc            # Cached bytecode of api.py
    │   ├── draw.cpython-38.pyc           # Cached bytecode of draw.py
    │   ├── ext.cpython-38.pyc            # Cached bytecode of ext.py
    │   ├── __init__.cpython-38.pyc       # Cached bytecode of __init__.py
    │   ├── metrics.cpython-38.pyc        # Cached bytecode of metrics.py
    │   ├── output_utils.cpython-38.pyc   # Cached bytecode of output_utils.py
    │   ├── st.cpython-38.pyc             # Cached bytecode of st.py
    │   └── utils.cpython-38.pyc          # Cached bytecode of utils.py
    ├── st.py                             # Utility for style transfer
    ├── tb_visualizer.py                  # TensorBoard visualizer utility
    └── utils.py                          # General utilities for the project

```

## **Dependencies**

Ensure all dependencies are installed by running:

```bash
pip install -r requirements.txt
```

Key dependencies include:

- Streamlit: For building the web interface.
- PyTorch: Deep learning framework for model implementation.
- Transformers: For utilizing Transformer models.
- Pillow: Image processing.
- Torchvision: For image transformations and pre-trained models.

## **Performance Tips**

- **Use GPU**: If your system supports GPU acceleration, PyTorch will automatically leverage it for faster model inference.
- **Run on Cloud**: You can deploy this app on platforms like Heroku, AWS, or Google Cloud for production-level scaling.
- **Batch Processing**: For processing multiple images at once, consider batching inputs to optimize performance.

## **Troubleshooting**

### **Common Errors and Solutions**

- **ModuleNotFoundError**: If you encounter errors about missing modules, ensure that all dependencies are installed and that your Python environment is correctly set up.
- **FileNotFoundError for Model Files**: Verify that `modelbest.ckpt`, `ingr_vocab.pkl`, and `instr_vocab.pkl` are placed in the correct directory (`Foodimg2Ing/data/`).
- **AttributeError in Streamlit**: If you receive errors like `'NoneType' object has no attribute 'format'`, ensure that the image generation function returns a valid image URL or handle cases where the image may be `None`.
- **CUDA Errors**: If you encounter CUDA-related warnings and you don't have a GPU or prefer to run on CPU, you can disable CUDA by setting the environment variable before running the app:

```bash
export CUDA_VISIBLE_DEVICES=-1
```

- **Port Already in Use**: If Streamlit indicates that the default port 8501 is in use, specify a different port:

```bash
streamlit run app.py --server.port 8502
```

## **Future Enhancements**

- **Real-time Recipe Adjustments**: Dynamically adjust recipes based on user preferences or dietary restrictions.
- **Cultural Integration**: Tailor recipes based on regional or cultural preferences.
- **Voice Commands**: Allow users to upload images and get recipes via voice commands.
- **Mobile App**: Convert the web app to a mobile app for easier accessibility.

## **Deploying to Heroku**

You can easily deploy this app to Heroku by following these steps:

1. **Install the Heroku CLI**: https://devcenter.heroku.com/articles/heroku-cli
2. **Login to Heroku**:

```bash
heroku login
```

3. **Create a new Heroku app**:

```bash
heroku create your-app-name
```

4. **Push the code**:

```bash
git push heroku main
```

For full deployment instructions, visit Heroku's Documentation.

## **Contributing**

Contributions are welcome! Please open an issue or submit a pull request on GitHub if you have suggestions or improvements.

## **Credits**

This project is built upon the efforts of the following repositories:

- Recipe Generation from Food Image by navassherif98
- [Recipe Generation from Food Image by navassherif98](https://github.com/navassherif98)
- Chef Transformer by chef-transformer
- [Chef Transformer by chef-transformer](https://github.com/chef-transformer)


## **License**

This project is licensed under the MIT License. See the LICENSE file for details.

## **Acknowledgments**

- The model is inspired by the work from Inverse Cooking: Recipe Generation from Food Images.
- Thanks to the developers of Streamlit for providing an easy way to build web apps.

## **Contact**

For any inquiries or support, please contact:

- Ganesh Adimalupu
- Email: Ganeshjohn253@gmail.com
- GitHub: GaneshAdimalupu
