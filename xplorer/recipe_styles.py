def apply_recipe_styles():
    """Apply recipe page styles, integrated with the global design system"""
    from home.styles import load_custom_css
    load_custom_css()  # Apply global styling first
    
    return """
    <style>
        /* Indian Recipe Explorer Styling Overrides */
        
        .results-count {
            font-size: 1.1rem;
            font-weight: 600;
            color: var(--text-secondary);
            margin: 1rem 0;
        }
        
        .results-count .highlight {
            color: var(--primary);
            font-weight: 800;
        }

        /* Customize Recipe Card Buttons */
        div[data-testid="stVerticalBlock"]:has(> div [class*="recipe-card-marker"]) button {
            background: rgba(255, 75, 75, 0.05) !important;
            color: var(--text-color) !important;
            border: 1px solid var(--card-border) !important;
            box-shadow: none !important;
            border-radius: 20px !important;
            padding: 0.35rem 1.2rem !important;
            font-size: 0.85rem !important;
            font-weight: 600 !important;
            transition: all 0.2s ease !important;
            width: 100% !important;
        }
        
        div[data-testid="stVerticalBlock"]:has(> div [class*="recipe-card-marker"]) button:hover {
            background: rgba(255, 75, 75, 0.12) !important;
            color: var(--primary) !important;
            border-color: var(--primary) !important;
            transform: translateY(-2px) !important;
        }

        /* Ingredients Grid */
        .ingredients-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 10px;
            margin-top: 15px;
        }
        
        .recipe-description {
            font-size: 0.95rem;
            color: var(--text-secondary);
            line-height: 1.5;
            margin: 12px 0;
            font-style: italic;
        }

        /* Image hover effects */
        .recipe-image {
            width: 100%;
            border-radius: 12px;
            margin: 1rem 0;
            transition: transform 0.3s ease;
            border: 1px solid var(--card-border);
        }
        
        .recipe-image:hover {
            transform: scale(1.01);
        }
        
        .recipe-image-placeholder {
            width: 100%;
            height: 200px;
            background: rgba(255, 75, 75, 0.02);
            border-radius: 12px;
            border: 1px dashed var(--card-border);
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 1rem 0;
        }
        
        .placeholder-content {
            text-align: center;
            color: var(--text-secondary);
        }
        
        .placeholder-content span {
            font-size: 2.5rem;
            display: block;
            margin-bottom: 5px;
        }

        /* Action Buttons Hover (HTML) */
        .action-button:hover {
            background: rgba(255, 75, 75, 0.1) !important;
            color: var(--primary) !important;
            border-color: var(--primary) !important;
            transform: translateY(-2px);
        }
    </style>
    """