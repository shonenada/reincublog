Reincublog
==========

A 'nice' little blog system built on Django.

Posts
-----

Posts have the following fields:

Title
    Title of the post, used to generate the URL as well as reference the post in the site.

Featured Image
    A single image to be associated with the post. Shown at the top of the blog post above the content.

Content
    Post content, written in TinyMCE in the Django admin. Accepts external images.

Categories
    Each post can be associated with any number of categories and will be shown in the category list.

Categories
----------

Name
    The name of the category.

Views
-----

There are three standard views to the blog:

- Index. The paginated, reverse chronologically ordered list of posts. Shows the post title, featured image and full text.

- Single post. The view for a single blog post shows the post itself with links to next and previous posts (if available) and links to category pages.

- Category list. For each category, a list of the posts in that category shown with title and featured image. List is reverse chronologically ordered and paginated.

Libraries
=========

Expected libraries required will be Sorl & TinyMCE, plus their dependencies.
