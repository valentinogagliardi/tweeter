A silly Twitter bot
---------------------------------------------------

Configuration
~~~~~~~~~~~~~

.. code:: python

    TWEETER = {
        "consumer_key": "",
        "consumer_secret": "",
        "access_token": "",
        "access_token_secret": "",
    }


Use
~~~~~~~~~~~~~
.. code:: python

    from tweeter.core import Tweeter

    TWEETER = {
        "consumer_key": "fill me!",
        "consumer_secret": "fill me!",
        "access_token": "fill me!",
        "access_token_secret": "fill me!",
    }


    class MyTweeter(Tweeter):
        def _build_tweet(self):
            return "Good morning friends!"


    a = MyTweeter(config=TWEETER)

    a.post_tweet()