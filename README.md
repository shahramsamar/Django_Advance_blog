# Django Advanced Blog

An advanced blog application built with Django, featuring a variety of modern web development techniques. The application includes functionalities such as user authentication, post categorization, comment systems, and more. This project aims to showcase best practices in Django web development.

![Alt](https://repobeats.axiom.co/api/embed/eabe6508a91fa38b4ace0060919094363916f544.svg "Repobeats analytics image")

## Features

- **User Authentication**: Users can register, log in, and manage their profiles.
- **Post Management**: Admins can create, update, and delete blog posts with a title, content, and featured images.
- **Category Support**: Posts can be categorized under different topics or themes.
- **Comment System**: Users can comment on blog posts, providing an interactive experience.
- **Tagging**: Posts can be tagged with multiple labels for better content discovery.
- **Rich Text Editor**: Enhanced text editing for creating posts using WYSIWYG.
- **Pagination**: Post listing includes pagination for easy navigation.

## Requirements

- **Python 3.x**
- **Django**: The main framework used for the project.
- **SQLite** (default database for Django, can be replaced with PostgreSQL or MySQL).
- **Other dependencies** listed in `requirements.txt`.

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/shahramsamar/Django_Advance_blog.git
    cd Django_Advance_blog
    ```

2. **Install Dependencies:**

    If you're using `pip`, run:

    ```bash
    pip install -r requirements.txt
    ```

3. **Apply Migrations**:

    Run the following command to set up the database schema:

    ```bash
    python manage.py migrate
    ```

4. **Create a Superuser (Admin)**:

    To manage blog posts and user accounts via the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

5. **Run the Development Server**:

    Start the development server with:

    ```bash
    python manage.py runserver
    ```

    The application will be accessible at `http://127.0.0.1:8000/`.

### How to Use

- **Login / Register**: Create an account or login with an existing user account.
- **Create Blog Post**: Admins can create, update, and delete blog posts.
- **Categorize Posts**: Assign each blog post to a category for better organization.
- **Post Comments**: Logged-in users can comment on posts.
- **Tags**: Add tags to posts for easy categorization.
- **Browse Blog**: Users can browse posts by category, tags, or author.

### Project Structure

- `blog/`: The main app that handles all blog-related functionality.
    - `models.py`: Defines models for posts, categories, comments, tags, etc.
    - `views.py`: Contains views for rendering blog pages, handling form submissions, and displaying posts.
    - `urls.py`: Routes the URLs for various blog-related views.
    - `forms.py`: Contains forms for creating and updating blog posts and comments.
    - `templates/`: Stores HTML templates for rendering the views.
        - `post_list.html`: Displays a list of all blog posts with pagination.
        - `post_detail.html`: Displays the details of an individual blog post along with comments.
        - `post_form.html`: Form used to create or update posts.
        - `category_list.html`: Displays posts categorized under specific topics.
    - `static/`: Contains any static files (CSS, JavaScript, images).
- `requirements.txt`: Lists all dependencies for the project (e.g., Django, Pillow for image handling).
- `manage.py`: The Django project management script for running the application.

### Contributing

Feel free to fork the project and submit pull requests for new features, improvements, or bug fixes.

### License

This project is open-source and available for educational purposes.

---

This `README.md` provides detailed instructions for setting up, using, and contributing to the **Django Advanced Blog** project. It includes features like user authentication, post management, categories, and comment systems, aimed at demonstrating advanced Django functionality.
