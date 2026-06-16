import base64
import numpy as np
import requests
import plotly.express as px
import streamlit as st
import os
from PIL import Image
from io import BytesIO

def img_to_base64(img_path):
    """Convert image file to base64 string"""
    with open(img_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def load_lottie_url(url: str):
    """Load and return Lottie animation from URL"""
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def check_dietary_restrictions(ingredients, restrictions):
    """Check ingredients against dietary restrictions"""
    restricted_ingredients = []
    for ingredient in ingredients:
        for restriction in restrictions:
            if restriction.lower() in ingredient.lower():
                restricted_ingredients.append(f"{ingredient} (contains {restriction})")
    return restricted_ingredients

def calculate_nutrition(ingredients):
    """Calculate mock nutrition facts for given ingredients"""
    return {
        "calories": np.random.randint(200, 800),
        "protein": np.random.randint(10, 30),
        "carbs": np.random.randint(20, 60),
        "fat": np.random.randint(10, 40),
        "fiber": np.random.randint(2, 8),
    }



def predict_from_image(uploaded_file):
    """Process uploaded image and generate recipe"""
    try:
        static_dir = os.path.join(os.getcwd(), "asset/Recipe Gen images/")
        os.makedirs(static_dir, exist_ok=True)

        image_path = os.path.join(static_dir, uploaded_file.name)
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        try:
            from Foodimg2Ing.output import output
            
            # Call output function which returns title, ingredients, recipe
            title, ingredients, recipe = output(image_path)

            # Handle title
            if isinstance(title, list):
                title = " ".join(title) if title else "Custom Recipe"
            elif not title:
                title = "Custom Recipe"

            # Clean and validate recipe steps
            if recipe:
                # Remove any error messages or invalid steps
                recipe = [
                    step
                    for step in recipe
                    if not any(
                        error_text in step.lower()
                        for error_text in ["reason:", "no", "eos", "found"]
                    )
                ]
                # Remove empty or single-character steps
                recipe = [step for step in recipe if len(step.strip()) > 1]

            # Ensure ingredients and recipe are lists
            ingredients = ingredients if ingredients and isinstance(ingredients, list) else []
            recipe = recipe if recipe else []

            return title, ingredients, recipe, image_path

        except Exception as e:
            st.error(f"Error processing image: {str(e)}")
            return None, None, None, None

    except Exception as e:
        st.error(f"Error saving image: {str(e)}")
        return None, None, None, None

def display_recipe_card(title, ingredients, instructions, nutrition, image_path=None):
    """Display recipe information in an enhanced, aesthetic card format"""
    # Inject container card marker
    st.markdown('<div class="recipe-card-marker"></div>', unsafe_allow_html=True)

    # Title section with elegant styling
    st.markdown(f'<h1 class="recipe-title">🍳 {title}</h1>', unsafe_allow_html=True)

    # Image and content layout
    cols = st.columns([1, 1])

    with cols[0]:
        if image_path:
            st.image(image_path, use_container_width=True, caption="")
            st.markdown("<br>", unsafe_allow_html=True)

        # Nutrition section with modern design
        st.markdown('<div class="nutrition-card" style="border: 1px solid var(--card-border); border-radius: 15px; padding: 1.5rem; background: rgba(255, 75, 75, 0.01);">', unsafe_allow_html=True)
        st.markdown("#### 📊 Nutrition Facts")

        # Visual progress rings for nutrition
        badges_html = '<div class="nutrition-grid" style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 15px; margin: 15px 0;">'
        
        colors = {
            "calories": "#FF4B4B",
            "protein": "#2ECC71",
            "carbs": "#3498DB",
            "fat": "#E67E22",
            "fiber": "#9B59B6"
        }
        
        daily_values = {
            "calories": 2000,
            "protein": 50,
            "carbs": 300,
            "fat": 65,
            "fiber": 25
        }
        
        for nutrient, value in nutrition.items():
            nut_key = nutrient.lower()
            try:
                val_clean = float(str(value).replace('g', '').strip())
            except ValueError:
                val_clean = 0.0
            
            dv = daily_values.get(nut_key, 100)
            pct = min(100.0, (val_clean / dv) * 100) if dv > 0 else 0.0
            
            # Circumference = 2 * pi * r = 2 * 3.14159 * 25 = 157.08
            offset = 157.08 - (pct / 100) * 157.08
            color = colors.get(nut_key, "#FF4B4B")
            unit = "" if nut_key == "calories" else "g"
            
            badges_html += f"""
                <div class="nutrition-badge" style="position: relative; display: flex; flex-direction: column; align-items: center; width: 75px;">
                    <svg class="progress-ring" width="60" height="60" style="transform: rotate(-90deg);">
                        <circle stroke="rgba(0,0,0,0.05)" stroke-width="4" fill="transparent" r="25" cx="30" cy="30"/>
                        <circle stroke="{color}" stroke-dasharray="157.08" stroke-dashoffset="{offset}" stroke-width="4" fill="transparent" r="25" cx="30" cy="30" style="transition: stroke-dashoffset 0.35s; transform-origin: 50% 50%;"/>
                    </svg>
                    <div style="position: absolute; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; font-size: 0.8rem; font-weight: 700; color: var(--text-color); top: 0; left: 0;">
                        {int(val_clean)}{unit}
                    </div>
                    <div style="margin-top: 5px; font-size: 0.75rem; font-weight: 600; color: var(--text-secondary); text-transform: uppercase;">{nutrient.capitalize()}</div>
                </div>
            """
        badges_html += '</div>'
        st.markdown(badges_html, unsafe_allow_html=True)

        # Interactive nutrition chart
        fig = px.pie(
            values=[float(str(v).replace('g','').strip()) for k, v in nutrition.items() if k.lower() != 'calories'],
            names=[k.capitalize() for k in nutrition.keys() if k.lower() != 'calories'],
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set3,
        )
        fig.update_layout(
            font=dict(family="Plus Jakarta Sans, sans-serif"),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            showlegend=True,
            legend=dict(
                orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5
            ),
            margin=dict(t=10, b=10, l=10, r=10),
            height=220,
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with cols[1]:
        # Ingredients section with enhanced styling
        st.markdown('<div class="recipe-section">', unsafe_allow_html=True)
        st.markdown("#### 🥗 Ingredients")
        for ingredient in ingredients:
            st.markdown(
                f'<div class="ingredient-item">• {ingredient}</div>',
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

        # Instructions section with step-by-step styling
        st.markdown('<div class="recipe-section">', unsafe_allow_html=True)
        st.markdown("#### 👩‍🍳 Instructions")
        for i, step in enumerate(instructions, 1):
            st.markdown(
                f'<div class="instruction-step"><span class="step-number">{i}</span>{step}</div>',
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

def load_image_from_url(url, target_size=None):
    """Load an image from a URL"""
    try:
        response = requests.get(url, timeout=10)
        img = Image.open(BytesIO(response.content))
        
        if target_size:
            img = img.resize(target_size)
        
        return img
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
        return None

def load_local_image(path, target_size=None):
    """Load an image from a local path"""
    try:
        img = Image.open(path)
        
        if target_size:
            img = img.resize(target_size)
        
        return img
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
        return None

def image_to_base64(img):
    """Convert a PIL image to base64 encoded string"""
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")