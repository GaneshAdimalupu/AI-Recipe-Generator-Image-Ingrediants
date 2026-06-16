import streamlit as st
from datetime import datetime
import base64
from PIL import Image
import io
from mongodb.db import get_database
from pages.posts import get_current_username
from post.models.db_schema import (
    posts_collection,
    likes_collection,
    bookmarks_collection,
    followers_collection
)

# Add users collection to store profile pictures
db = get_database()
users_collection = db["users"]

def render_instagram_grid(username, posts):
    """Render posts in an Instagram-like grid layout"""
    st.markdown("""
    <style>
        .instagram-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            width: 100%;
        }
        
        .post-item {
            position: relative;
            overflow: hidden;
            aspect-ratio: 1 / 1;
            width: 100%;
            cursor: pointer;
            transition: transform 0.3s ease;
        }
        
        .post-item:hover {
            transform: scale(1.05);
            z-index: 10;
        }
        
        .post-image {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        
        .post-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.4);
            display: flex;
            justify-content: center;
            align-items: center;
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        
        .post-item:hover .post-overlay {
            opacity: 1;
        }
        
        .post-stats {
            color: white;
            display: flex;
            gap: 15px;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Instagram-like grid container
    st.markdown('<div class="instagram-grid">', unsafe_allow_html=True)
    
    for post in posts:
        # Try to decode and display image
        try:
            if post.get('image'):
                image = Image.open(io.BytesIO(base64.b64decode(post['image'])))
            else:
                # Fallback to placeholder
                image = Image.open("https://via.placeholder.com/300")
            
            # Convert image to base64 for HTML display
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            img_base64 = base64.b64encode(buffered.getvalue()).decode()
            
            # Post item with overlay
            st.markdown(f"""
            <div class="post-item">
                <img src="data:image/png;base64,{img_base64}" class="post-image" alt="Post Image">
                <div class="post-overlay">
                    <div class="post-stats">
                        <span>❤️ {post.get('likes', 0)}</span>
                        <span>💬 {post.get('comments_count', 0)}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        except Exception as e:
            # Fallback for any image processing errors
            st.markdown(f"""
            <div class="post-item">
                <img src="https://via.placeholder.com/300" class="post-image" alt="Placeholder">
                <div class="post-overlay">
                    <div class="post-stats">
                        <span>❤️ 0</span>
                        <span>💬 0</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Close grid container
    st.markdown('</div>', unsafe_allow_html=True)

def get_profile_stats(username):
    """Get user's profile statistics"""
    # Get post count
    posts_count = posts_collection.count_documents({"user": username})
    
    # Get followers count
    followers_count = followers_collection.count_documents({"following": username})
    
    # Get following count
    following_count = followers_collection.count_documents({"follower": username})
    
    return posts_count, followers_count, following_count

def get_profile_picture(username):
    """Get user's profile picture from the database"""
    user = users_collection.find_one({"username": username})
    if user and user.get("profile_picture"):
        return user["profile_picture"]
    return None


def upload_profile_picture(username):
    """Handle profile picture upload and save to database"""
    uploaded_file = st.file_uploader("Change Profile Picture", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file:
        try:
            # Read the file and resize for optimization
            image = Image.open(uploaded_file)
            
            # Resize to a reasonable profile picture size (300x300)
            image = image.resize((300, 300))
            
            # Convert to RGB if it's RGBA (to ensure compatibility)
            if image.mode == 'RGBA':
                image = image.convert('RGB')
            
            # Save to bytes buffer
            buffered = io.BytesIO()
            image.save(buffered, format="JPEG", quality=85)
            
            # Convert to base64
            base64_image = base64.b64encode(buffered.getvalue()).decode()
            
            # Update user's profile picture in database
            # Use upsert=True to create the user document if it doesn't exist
            result = users_collection.update_one(
                {"username": username},
                {"$set": {
                    "profile_picture": base64_image,
                    "updated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }},
                upsert=True
            )
            
            return base64_image, result.modified_count > 0 or result.upserted_id is not None
            
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")
            return None, False
    
    return None, False

def render_profile_page(username):
    """Render the user profile page with profile picture database support"""
    # Apply custom CSS
    st.markdown("""
    <style>
        /* Profile Section */
        .profile-section {
            padding: 20px;
            margin-bottom: 30px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        
        .profile-header {
            display: flex;
            align-items: flex-start;
            width: 100%;
            margin-bottom: 2rem;
        }
        
        .profile-picture-container {
            position: relative;
            margin-right: 2rem;
        }
        
        .profile-picture {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid #fff;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .profile-avatar {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            background-color: #f0f0f0;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3rem;
            color: #555;
            border: 3px solid #fff;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .edit-button {
            position: absolute;
            bottom: 5px;
            right: 5px;
            background-color: #f0f0f0;
            border-radius: 50%;
            width: 30px;
            height: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }
        
        /* Stats Section */
        .stats-container {
            display: flex;
            justify-content: space-around;
            width: 100%;
            margin: 20px 0;
            text-align: center;
        }
        
        .stat-item {
            display: flex;
            flex-direction: column;
        }
        
        /* Bio Section */
        .bio-section {
            width: 100%;
            margin: 20px 0;
            padding: 10px;
        }
        
        /* Posts Grid */
        .posts-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-top: 20px;
            width: 100%;
        }
        
        .grid-post {
            aspect-ratio: 1;
            object-fit: cover;
            width: 100%;
            transition: transform 0.2s;
        }
        
        .grid-post:hover {
            transform: scale(1.02);
        }
    </style>
    """, unsafe_allow_html=True)
    
    from home.styles import load_custom_css
    load_custom_css()
    
    # Get user stats
    posts_count, followers_count, following_count = get_profile_stats(username)
    
    # Create container for profile section
    st.markdown('<div class="profile-section-marker"></div>', unsafe_allow_html=True)
    
    # Left column - Profile picture
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Check if user has a profile picture in database
        profile_pic = get_profile_picture(username)
        
        if profile_pic:
            # Display the user's profile picture from database
            st.markdown(f"""
                <div class="profile-picture-container" style="text-align: center; margin-bottom: 15px;">
                    <img src="data:image/jpeg;base64,{profile_pic}" style="width: 130px; height: 130px; border-radius: 50%; border: 3px solid var(--primary); object-fit: cover; box-shadow: var(--shadow);">
                </div>
            """, unsafe_allow_html=True)
        else:
            # Display avatar from dicebear as fallback
            st.markdown(f"""
                <div class="profile-picture-container" style="text-align: center; margin-bottom: 15px;">
                    <img src="https://api.dicebear.com/6.x/avataaars/svg?seed={username}" style="width: 130px; height: 130px; border-radius: 50%; border: 3px solid var(--primary); object-fit: cover; box-shadow: var(--shadow);">
                </div>
            """, unsafe_allow_html=True)
        
        # Profile picture upload functionality
        show_upload = st.checkbox("Change profile picture", key="show_upload")
        
        if show_upload:
            new_pic, success = upload_profile_picture(username)
            if success:
                st.success("Profile picture updated successfully!")
                # Add JavaScript to reload the page after successful upload
                st.markdown("""
                    <script>
                        setTimeout(function() {
                            window.location.reload();
                        }, 2000);
                    </script>
                """, unsafe_allow_html=True)
    
    with col2:
        # Username and Edit Profile Button
        st.markdown(f"""
            <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 10px;">
                <span style="font-size: 1.8rem; font-weight: 800; color: var(--text-color);">@{username}</span>
            </div>
        """, unsafe_allow_html=True)
        
        # Edit profile button
        if st.button("✏️ Edit Bio", key="edit_profile"):
            st.session_state.editing_profile = True
        
        # Stats Row (HTML for perfect control)
        st.markdown(f"""
            <div style="display: flex; gap: 30px; margin: 15px 0;">
                <div>
                    <div style="font-size: 1.3rem; font-weight: 800; color: var(--primary);">{posts_count}</div>
                    <div style="font-size: 0.75rem; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.5px;">Posts</div>
                </div>
                <div>
                    <div style="font-size: 1.3rem; font-weight: 800; color: var(--primary);">{followers_count}</div>
                    <div style="font-size: 0.75rem; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.5px;">Followers</div>
                </div>
                <div>
                    <div style="font-size: 1.3rem; font-weight: 800; color: var(--primary);">{following_count}</div>
                    <div style="font-size: 0.75rem; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.5px;">Following</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Bio Section
        user_data = users_collection.find_one({"username": username}) or {}
        bio = user_data.get("bio", "🧑‍🍳 Food enthusiast and recipe creator")
        location = user_data.get("location", "📍 Making delicious meals and sharing them with the world")
        
        # If in editing mode, show form to update bio and location
        if st.session_state.get("editing_profile", False):
            with st.form("profile_edit_form"):
                new_bio = st.text_area("Bio", value=bio)
                new_location = st.text_input("Location", value=location)
                
                if st.form_submit_button("Save Profile"):
                    # Update user profile in database
                    users_collection.update_one(
                        {"username": username},
                        {"$set": {
                            "bio": new_bio,
                            "location": new_location,
                            "updated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        }},
                        upsert=True
                    )
                    st.session_state.editing_profile = False
                    st.success("Profile updated!")
                    st.rerun()
        else:
            # Display bio and location
            st.markdown(f"""
                <div style="margin-top: 10px; line-height: 1.5;">
                    <div style="font-weight: 500; color: var(--text-color); margin-bottom: 5px;">{bio}</div>
                    <div style="font-size: 0.9rem; color: var(--text-secondary);">{location}</div>
                </div>
            """, unsafe_allow_html=True)
    
    # Posts Grid Section
    st.markdown("### Posts")
    
    # Get user's posts
    posts = list(posts_collection.find({"user": username}).sort("time", -1))
    
    # Create grid layout
    if posts:
        # Split posts into rows of 3
        for i in range(0, len(posts), 3):
            cols = st.columns(3)
            for j, col in enumerate(cols):
                if i + j < len(posts):
                    post = posts[i + j]
                    with col:
                        # Display post image or placeholder
                        if post.get('image'):
                            try:
                                image = Image.open(io.BytesIO(base64.b64decode(post['image'])))
                                st.image(image, use_container_width=True)
                            except Exception:
                                st.image("https://via.placeholder.com/300", use_container_width=True)
                        else:
                            st.image("https://via.placeholder.com/300", use_container_width=True)
                        
                        # Post stats
                        st.markdown(f"""
                            ❤️ {post.get('likes', 0)} &nbsp;&nbsp; 
                            💬 {post.get('comments_count', 0)}
                        """)
    else:
        st.info("No posts yet! Share your first recipe to get started.")



def main():
    """Main function to handle the profile page"""
    # Initialize session state for profile editing
    if "editing_profile" not in st.session_state:
        st.session_state.editing_profile = False
    
    if not st.session_state.get("LOGGED_IN", False):
        st.switch_page("streamlit_app.py")
        return
    
    # Get current user with improved error handling
    username = get_current_username()

    if not username:
        st.error("Please log in to access your profile.")
        st.error("If you're seeing this message after logging in, please try refreshing the page.")
        if st.button("Return to Login"):
            st.switch_page("streamlit_app.py")
        return
    
    try:
        render_profile_page(username)
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.error("Please try refreshing the page. If the error persists, contact support.")


if __name__ == "__main__":
    main()