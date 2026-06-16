import streamlit as st

def load_custom_css():
    """Load all custom CSS styles for the application"""
    st.markdown(
        """
        <style>
        /* Global CSS and Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
        
        :root {
            --primary: #FF4B4B;
            --primary-light: #FF8533;
            --primary-rgb: 255, 75, 75;
            --bg-gradient: linear-gradient(135deg, rgba(255, 75, 75, 0.03) 0%, rgba(255, 133, 51, 0.03) 100%);
            --card-bg: rgba(255, 255, 255, 0.85);
            --card-border: rgba(255, 255, 255, 0.45);
            --text-color: #2D3748;
            --text-secondary: #718096;
            --shadow: 0 10px 30px rgba(31, 38, 135, 0.04);
            --shadow-hover: 0 15px 35px rgba(31, 38, 135, 0.08);
            --border-radius: 20px;
        }

        @media (prefers-color-scheme: dark) {
            :root {
                --bg-gradient: linear-gradient(135deg, rgba(15, 15, 15, 0.95) 0%, rgba(30, 30, 30, 0.95) 100%);
                --card-bg: rgba(26, 26, 29, 0.8);
                --card-border: rgba(255, 255, 255, 0.08);
                --text-color: #F7FAFC;
                --text-secondary: #A0AEC0;
                --shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
                --shadow-hover: 0 15px 35px rgba(0, 0, 0, 0.45);
            }
        }

        /* General Layout overrides */
        html, body, [class*="css"], [class*="st-"] {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }
        
        [data-testid="stAppViewContainer"] {
            background: var(--bg-gradient);
            color: var(--text-color);
        }

        /* Card System using parent selector on stVerticalBlock containing a marker */
        div[data-testid="stVerticalBlock"]:has(> div[data-testid="element-container"] [class*="-marker"]) {
            background: var(--card-bg) !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            border: 1px solid var(--card-border) !important;
            border-radius: var(--border-radius) !important;
            padding: 2.5rem !important;
            box-shadow: var(--shadow) !important;
            margin-bottom: 2rem !important;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
        }

        div[data-testid="stVerticalBlock"]:has(> div[data-testid="element-container"] [class*="-marker"]):hover {
            transform: translateY(-4px) !important;
            box-shadow: var(--shadow-hover) !important;
        }

        /* Remove default Streamlit cards/borders if nested under markers to prevent double borders */
        div[data-testid="stVerticalBlock"]:has(> div[data-testid="element-container"] [class*="-marker"]) div[data-testid="stVerticalBlock"] {
            border: none !important;
            box-shadow: none !important;
            background: transparent !important;
            padding: 0 !important;
        }

        /* Custom headers styling */
        .page-header {
            text-align: center;
            margin-bottom: 2.5rem;
            animation: fadeIn 0.8s ease-out;
        }
        .page-header h1 {
            font-size: 2.8rem;
            font-weight: 800;
            background: linear-gradient(90deg, var(--primary), var(--primary-light));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }
        .page-header p {
            font-size: 1.1rem;
            color: var(--text-secondary);
        }

        /* Buttons styling */
        .stButton > button {
            background: linear-gradient(90deg, var(--primary), var(--primary-light)) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            font-weight: 600 !important;
            padding: 0.6rem 2rem !important;
            box-shadow: 0 4px 15px rgba(255, 75, 75, 0.2) !important;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
        }

        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(255, 75, 75, 0.35) !important;
            opacity: 0.95;
        }

        .stButton > button:active {
            transform: translateY(1px) !important;
        }

        /* Secondary Button Override (for Clear / Back buttons) */
        div[data-testid="element-container"]:has(button:contains("Clear")),
        div[data-testid="element-container"]:has(button:contains("Previous")),
        div[data-testid="element-container"]:has(button:contains("Return")),
        div[data-testid="element-container"]:has(button:contains("Cancel")) {
            /* Handled dynamically if Streamlit supports it, else standard style applies */
        }

        /* Input Elements Styling */
        input, select, textarea {
            border-radius: 10px !important;
            border: 1px solid var(--card-border) !important;
            background-color: rgba(255, 255, 255, 0.05) !important;
            transition: all 0.3s ease !important;
        }

        input:focus, select:focus, textarea:focus {
            border-color: var(--primary) !important;
            box-shadow: 0 0 0 2px rgba(255, 75, 75, 0.1) !important;
        }

        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 1.5rem !important;
            background-color: rgba(255, 75, 75, 0.03) !important;
            border-radius: 12px !important;
            padding: 0.5rem !important;
            border: 1px solid var(--card-border) !important;
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 48px !important;
            border-radius: 8px !important;
            color: var(--text-secondary) !important;
            font-weight: 600 !important;
            border: none !important;
            transition: all 0.3s ease !important;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            color: var(--primary) !important;
            background-color: rgba(255, 75, 75, 0.05) !important;
        }

        .stTabs [aria-selected="true"] {
            color: var(--primary) !important;
            background-color: rgba(255, 75, 75, 0.08) !important;
        }

        /* Circular progress rings for nutrition */
        .nutrition-grid {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            gap: 1.5rem;
            margin: 1.5rem 0;
            padding: 1.5rem;
            background: rgba(255, 75, 75, 0.02);
            border-radius: 16px;
            border: 1px solid var(--card-border);
        }

        .nutrition-badge {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            width: 100px;
        }

        .progress-ring {
            transform: rotate(-90deg);
        }

        .progress-ring__circle {
            transition: stroke-dashoffset 0.35s;
            transform-origin: 50% 50%;
        }

        .nutrition-badge__value {
            position: absolute;
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--text-color);
            margin-top: 28px;
        }

        .nutrition-badge__label {
            margin-top: 0.8rem;
            font-size: 0.85rem;
            font-weight: 600;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        /* Recipe sections inner styling */
        .recipe-section {
            background-color: rgba(255, 75, 75, 0.02);
            border-radius: 15px;
            padding: 1.5rem;
            margin-bottom: 1.2rem;
            border: 1px solid var(--card-border);
        }

        .recipe-title {
            color: var(--primary);
            font-size: 2.2rem;
            font-weight: 800;
            margin-bottom: 1rem;
            text-align: center;
            background: linear-gradient(90deg, var(--primary), var(--primary-light));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .ingredient-item {
            background-color: var(--card-bg);
            border-radius: 10px;
            padding: 0.6rem 1.2rem;
            margin-bottom: 0.6rem;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.02);
            border: 1px solid var(--card-border);
            font-size: 0.95rem;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .instruction-step {
            background-color: var(--card-bg);
            border-radius: 12px;
            padding: 1.2rem;
            margin-bottom: 0.8rem;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.02);
            border: 1px solid var(--card-border);
            display: flex;
            gap: 12px;
            line-height: 1.5;
        }

        .step-number {
            background: linear-gradient(90deg, var(--primary), var(--primary-light));
            color: white;
            border-radius: 50%;
            width: 24px;
            height: 24px;
            min-width: 24px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 0.85rem;
        }
        
        /* Lottie container centering */
        div[data-testid="stVerticalBlock"]:has(> div[data-testid="element-container"] .lottie-container) {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            width: 100% !important;
        }

        /* Animation keyframes */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
