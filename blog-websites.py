import streamlit as st
import os
from datetime import datetime

# Set up the blog data
blog_posts = [
    {
        "title": "Introduction to Streamlit",
        "content": "Streamlit is a simple and powerful tool to create web applications with minimal code.",
        "author": "John Doe",
        "date": "2024-01-19"
    },
    {
        "title": "Building a Blog with Streamlit",
        "content": "In this tutorial, we'll create a simple blog using Streamlit.",
        "author": "Jane Doe",
        "date": "2024-01-20"
    }
]

# Function to render a blog post
def render_post(post):
    st.write(f"## {post['title']}")
    st.write(f"**Author:** {post['author']}")
    st.write(f"**Date:** {post['date']}")
    st.write(post['content'])

# Streamlit app
def main():
    st.title("Simple Blog with Streamlit")

    # Sidebar for adding new posts
    st.sidebar.header("Add New Post")
    new_title = st.sidebar.text_input("Title:")
    new_content = st.sidebar.text_area("Content:")
    new_author = st.sidebar.text_input("Author:")
    add_post_button = st.sidebar.button("Add Post")

    if add_post_button:
        if new_title and new_content and new_author:
            new_post = {
                "title": new_title,
                "content": new_content,
                "author": new_author,
                "date": datetime.now().strftime("%Y-%m-%d")
            }
            blog_posts.append(new_post)
            st.success("New post added successfully!")

    # Display existing posts
    st.header("Blog Posts")
    for post in reversed(blog_posts):  # Show the latest post first
        render_post(post)
        st.markdown("---")  # Separator between posts

if __name__ == "__main__":
    main()
