oriflamme
=========

Django class-based views with flags.

How to install
--------------

**Warning:** not tested yet. I think it doesn't quite work.

From GitHub
~~~~~~~~~~~

Run the command::

    pip install https://github.com/jleeothon/oriflamme.git

Packaging yourself
~~~~~~~~~~~~~~~~~~

1. Download the ``oriflamme`` folder.
2. Run ``python setup.py sdist``. This will generate a ``.tar.gz`` file inside a ``dist`` folder.
3. install by running ``pip install path/to/your/dist/oriflamme-0.1.tar.gz``

Use case
--------

Sometimes you want to set certain flags (i.e. boolean objects) to exist and probably be ``True`` in some of your templates. Maybe for one or two templates, you don't really need to install an app. Nonetheless, let's say you have *types* of templates or views; the easiest example could be *creating* views, *updating* views, etc.

When using class based views, adding a couple of variables to the context dictionary can be a bit of a fuss::

    # views.py
    
    class CreateCookieView(CreateView):
    
        model = Cookie
        
        def get_context_data(self, **kwargs):
            context = super(CreateCookieView, self).get_context_data(**kwargs)
            context['is_creating'] = True
            context['should_show_red_button'] = True
            return context

Now, let's say you also need those variables to be set in the CreateIceCreamView and CreateBubbleTeaView.

Instead of repeating the forementioned lines, you can add the flags in a single line using the ``FlagMixin``::

    # views.py
    
    from oriflamme import FlagMixin
    
    class CreateCookieView(FlagMixin, CreateView):
    
        template_flags = ('is_creating', 'should_show_red_button')

..

    You can use this in custom parent class-based views, or individual class-based views as needed.
