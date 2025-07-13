# Jonny's Blog

A personal blog built with Django featuring a modern design and interactive features.

## Features

- **Blog Posts**: Create and manage blog posts with rich content
- **Comments System**: Users can leave comments on posts
- **Read Later**: Save posts to read later with session-based storage
- **Tags**: Categorize posts with tags
- **Responsive Design**: Modern, mobile-friendly interface
- **Dynamic Footer**: Automatically updates with current year

## Tech Stack

- **Backend**: Django 5.2.2
- **Database**: SQLite (development)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with responsive design

## Project Structure

```
my_site/
├── blog/                 # Main blog application
│   ├── models.py        # Post, Author, Tag, Comment models
│   ├── views.py         # Class-based views
│   ├── templates/       # HTML templates
│   └── static/          # CSS and static files
├── config/              # Django settings
├── templates/           # Base templates
└── static/             # Global static files
```

## Key Features

### Models
- **Post**: Blog posts with title, content, excerpt, image, and tags
- **Author**: Blog authors with name and email
- **Tag**: Categories for posts
- **Comment**: User comments on posts

### Views
- **Home**: Latest 3 posts
- **All Posts**: Complete blog listing
- **Post Detail**: Individual post with comments
- **Read Later**: Session-based post storage

### Interactive Features
- **Comment System**: Users can leave comments on posts
- **Read Later**: Toggle posts to/from read later list
- **Responsive Design**: Works on all device sizes

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd my_site
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

6. Visit http://127.0.0.1:8000/ to see your blog!

## Usage

### Adding Posts
1. Go to Django admin at `/admin/`
2. Add authors, tags, and posts
3. Posts will automatically appear on your blog

### Features
- **Home Page**: Shows latest 3 posts
- **All Posts**: Browse all blog posts
- **Post Details**: Read full posts with comments
- **Read Later**: Save posts for later reading

## Development

This project was built entirely without AI assistance, demonstrating:
- Strong Django fundamentals
- Clean code architecture
- Modern web development practices
- User experience considerations

## License

© 2024 Jonny's Blog. All rights reserved.

---

Built with Django & ❤️ 