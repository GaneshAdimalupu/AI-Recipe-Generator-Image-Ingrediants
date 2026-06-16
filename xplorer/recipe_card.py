import streamlit as st
from xplorer.recipe_helpers import (
    parse_ingredients,
    parse_instructions,
    is_recipe_saved,
    toggle_recipe_save
)
import requests
from PIL import Image
from io import BytesIO

def load_image(url):
    """Load image from URL with error handling"""
    try:
        response = requests.get(url, timeout=5)
        img = Image.open(BytesIO(response.content))
        return img
    except Exception as e:
        return None

def render_recipe_card(recipe, current_user, index):
    """Render a single recipe card with animations"""
    with st.container():
        st.markdown('<div class="recipe-card-marker"></div>', unsafe_allow_html=True)
        st.markdown(f"""
            <div class="recipe-header" style="padding-bottom: 12px; border-bottom: 1px solid var(--card-border); margin-bottom: 15px;">
                <h2 class="recipe-title" style="margin: 0 0 10px 0; font-size: 1.6rem; color: var(--primary); font-weight: 700;">{recipe['name']}</h2>
                <div class="recipe-info" style="display: flex; gap: 10px; flex-wrap: wrap;">
                    <span class="info-tag" style="background: rgba(255, 75, 75, 0.08); color: var(--primary); padding: 4px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; display: flex; align-items: center; gap: 5px;">
                        <span>🍽️</span> <span>{recipe['course']}</span>
                    </span>
                    <span class="info-tag" style="background: rgba(255, 75, 75, 0.08); color: var(--primary); padding: 4px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; display: flex; align-items: center; gap: 5px;">
                        <span>👨‍🍳</span> <span>{recipe['cuisine']}</span>
                    </span>
                    <span class="info-tag" style="background: rgba(255, 75, 75, 0.08); color: var(--primary); padding: 4px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; display: flex; align-items: center; gap: 5px;">
                        <span>🥗</span> <span>{recipe['diet']}</span>
                    </span>
                    <span class="info-tag" style="background: rgba(255, 75, 75, 0.08); color: var(--primary); padding: 4px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; display: flex; align-items: center; gap: 5px;">
                        <span>⏱️</span> <span>{recipe['prep_time']}</span>
                    </span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Save button
        col1, col2 = st.columns([6, 1])
        with col2:
            is_saved = is_recipe_saved(recipe['name'], current_user)
            if st.button(
                "❤️" if is_saved else "🤍",
                key=f"save_{recipe['name']}_{index}",
                help="Save recipe to your collection"
            ):
                if current_user:
                    is_saved = toggle_recipe_save(
                        recipe['name'],
                        recipe.to_dict(),
                        current_user
                    )
                    st.rerun()
                else:
                    st.warning("Please log in to save recipes")

        # Description
        if recipe.get("description"):
            st.markdown(f"""
                <div class="recipe-description">
                    {recipe["description"]}
                </div>
            """, unsafe_allow_html=True)
        
        # Image display with loading state
        if recipe.get('image_url') and recipe.get('image_available', True):
            with st.container():
                # Show loading spinner while image loads
                with st.spinner('Loading image...'):
                    img = load_image(recipe['image_url'])
                    if img:
                        # Display image with enhanced styling
                        st.markdown("""
                            <style>
                                .recipe-image {
                                    width: 100%;
                                    border-radius: 10px;
                                    margin: 1rem 0;
                                    transition: transform 0.3s ease;
                                }
                                .recipe-image:hover {
                                    transform: scale(1.02);
                                }
                            </style>
                        """, unsafe_allow_html=True)
                        st.image(img, use_container_width=True, caption=recipe['name'], 
                                output_format="PNG", clamp=True)
                    else:
                        # Display placeholder if image fails to load
                        st.markdown("""
                            <div class="recipe-image-placeholder">
                                <div class="placeholder-content">
                                    <span>🍲</span>
                                    <p>Image not available</p>
                                </div>
                            </div>
                            <style>
                                .recipe-image-placeholder {
                                    width: 100%;
                                    height: 300px;
                                    background: #f5f5f5;
                                    border-radius: 10px;
                                    display: flex;
                                    align-items: center;
                                    justify-content: center;
                                    margin: 1rem 0;
                                }
                                .placeholder-content {
                                    text-align: center;
                                    color: #666;
                                }
                                .placeholder-content span {
                                    font-size: 3rem;
                                }
                                .placeholder-content p {
                                    margin-top: 0.5rem;
                                }
                            </style>
                        """, unsafe_allow_html=True)


        # Recipe content in tabs
        tab1, tab2 = st.tabs(["📝 Ingredients", "📋 Instructions"])
        
        with tab1:
            render_ingredients(recipe.get('ingredients', ''))
            
        with tab2:
            render_instructions(recipe.get('instructions', ''))

        # Action buttons
        st.markdown("""
            <div class="recipe-actions" style="display: flex; gap: 10px; margin-top: 15px; border-top: 1px solid var(--card-border); padding-top: 12px;">
                <button class="action-button share-button" style="background: transparent; border: 1px solid var(--card-border); border-radius: 20px; padding: 6px 16px; font-size: 0.85rem; color: var(--text-color); font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 5px; transition: all 0.2s;">
                    <span>🔗</span> <span>Share Recipe</span>
                </button>
                <button class="action-button print-button" style="background: transparent; border: 1px solid var(--card-border); border-radius: 20px; padding: 6px 16px; font-size: 0.85rem; color: var(--text-color); font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 5px; transition: all 0.2s;">
                    <span>🖨️</span> <span>Print Recipe</span>
                </button>
            </div>
            <script>
                // Add hover interactions dynamically via inline script or just CSS
            </script>
        """, unsafe_allow_html=True)

def render_ingredients(ingredients_str):
    """Render ingredients list with animations"""
    ingredients = parse_ingredients(ingredients_str)
    if ingredients:
        st.markdown('<div class="ingredients-grid">', unsafe_allow_html=True)
        for i, ing in enumerate(ingredients):
            st.markdown(f"""
                <div class="ingredient-item" style="animation-delay: {i * 0.1}s">
                    <div class="ingredient-quantity">{ing['quantity']}</div>
                    <div class="ingredient-name">{ing['name']}</div>
                </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

def render_instructions(instructions_str):
    """Render instructions with animations"""
    instructions = parse_instructions(instructions_str)
    for i, step in enumerate(instructions, 1):
        st.markdown(f"""
            <div class="instruction-step" style="animation-delay: {i * 0.1}s">
                <div class="step-number">{i}</div>
                {step}
            </div>
        """, unsafe_allow_html=True)