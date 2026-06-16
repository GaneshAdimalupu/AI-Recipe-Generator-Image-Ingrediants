def get_styles():
    """Returns Instagram-like CSS styles for the social feed, integrated with the global design system"""
    return """
    <style>
        /* Social Feed Specific Styles */
        
        /* Post Interaction Buttons Styling */
        div[data-testid="stVerticalBlock"]:has(> div [class*="post-card-marker"]) button {
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
        
        div[data-testid="stVerticalBlock"]:has(> div [class*="post-card-marker"]) button:hover {
            background: rgba(255, 75, 75, 0.12) !important;
            color: var(--primary) !important;
            border-color: var(--primary) !important;
            transform: translateY(-2px) !important;
        }

        /* Post tags styling */
        .tag-container {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin: 12px 0;
        }
        
        .tag {
            background-color: rgba(255, 75, 75, 0.08);
            color: var(--primary);
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            transition: all 0.2s;
        }
        
        .tag:hover {
            background-color: rgba(255, 75, 75, 0.15);
            transform: scale(1.05);
        }
        
        /* Comments Section */
        .comments-section {
            padding: 12px 16px;
            border-top: 1px solid var(--card-border);
            max-height: 300px;
            overflow-y: auto;
            background: rgba(255, 75, 75, 0.01);
            border-radius: 12px;
            margin-top: 10px;
        }
        
        .comment-item {
            margin-bottom: 12px;
            display: flex;
            align-items: flex-start;
            gap: 10px;
            animation: fadeIn 0.3s ease-out;
        }
        
        .comment-avatar {
            width: 28px;
            height: 28px;
            border-radius: 50%;
            border: 1px solid var(--card-border);
        }
        
        .comment-content {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            padding: 8px 12px;
            border-radius: 12px;
            flex-size: 1;
        }
        
        .comment-username {
            font-weight: 700;
            font-size: 0.85rem;
            color: var(--primary);
            margin-bottom: 2px;
        }
        
        .comment-text {
            font-size: 0.85rem;
            color: var(--text-color);
            line-height: 1.4;
        }
        
        .comment-time {
            font-size: 0.75rem;
            color: var(--text-secondary);
            margin-top: 4px;
        }

        /* Stories Bar */
        .stories-bar {
            display: flex;
            overflow-x: auto;
            padding: 16px;
            margin-bottom: 24px;
            background: var(--card-bg);
            border-radius: var(--border-radius);
            border: 1px solid var(--card-border);
            box-shadow: var(--shadow);
        }
        
        .story-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-right: 16px;
            cursor: pointer;
        }
        
        .story-avatar-container {
            width: 62px;
            height: 62px;
            border-radius: 50%;
            background: linear-gradient(45deg, var(--primary), var(--primary-light));
            padding: 2px;
            margin-bottom: 6px;
        }
        
        .story-avatar {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            border: 2px solid var(--card-bg);
            object-fit: cover;
        }
        
        .story-username {
            font-size: 0.75rem;
            font-weight: 600;
            color: var(--text-color);
            max-width: 64px;
            text-overflow: ellipsis;
            overflow: hidden;
            white-space: nowrap;
            text-align: center;
        }
        
        /* Explore Grid */
        .explore-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            margin-bottom: 24px;
        }
        
        .explore-item {
            position: relative;
            aspect-ratio: 1;
            overflow: hidden;
            border-radius: 12px;
            border: 1px solid var(--card-border);
            cursor: pointer;
            box-shadow: var(--shadow);
            transition: all 0.3s ease;
        }
        
        .explore-item:hover {
            transform: translateY(-4px);
            box-shadow: var(--shadow-hover);
        }
        
        .explore-image {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        
        .explore-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.4);
            opacity: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            transition: opacity 0.3s;
        }
        
        .explore-item:hover .explore-overlay {
            opacity: 1;
        }
        
        .explore-stats {
            display: flex;
            color: white;
            font-weight: 700;
            gap: 15px;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .explore-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }
    </style>
    """

def apply_post_styles():
    """Apply the social feed styles to the current Streamlit page"""
    import streamlit as st
    from home.styles import load_custom_css
    load_custom_css()  # Apply global styles first
    st.markdown(get_styles(), unsafe_allow_html=True)