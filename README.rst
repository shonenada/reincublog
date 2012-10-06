Reincublog
==========

A 'nice' little blog system built on Django.

Posts
-----

Posts have the following fields:

Author
    A user that is shown as the author.

Title
    Title of the post, used to generate the URL as well as reference the post in the site.

Featured Image
    A single image to be associated with the post. Shown at the top of the blog post above the content.

Content
    Post content, written in TinyMCE in the Django admin. Accepts external images.

Published Date
    Date that the post is published and used for ordering in post lists.

Views
-----

There are two standard views to the blog:

- Index. The paginated, reverse chronologically ordered list of posts. Shows the post title, featured image and full text.

- Single post. The view for a single blog post shows the post itself with links to next and previous posts (if available) and links to category pages.

Libraries
=========

Expected libraries required will be:

- Sorl
- TinyMCE
- Plus sitemaps https://docs.djangoproject.com/en/1.4/ref/contrib/sitemaps/
- Comments https://docs.djangoproject.com/en/1.4/ref/contrib/comments/

... Plus their dependencies.

Install
=======

- Clone the repository and ``cd`` into it.
- Create virtualenv in the ``env`` folder, this should put a python binary at ``env/bin/python``::

    virtualenv --python [your python path]/python env

- Install the required libs with ``pip``, they are in the ``requirements.txt`` file.
- Make a copy of ``riblog/local_settings.example.py`` to ``riblog/local_settings.py`` and configure for your db.
- Create the required DB, migrate with south.
- All tests should run too :D
