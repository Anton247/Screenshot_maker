# Python Screenshots Maker

A dead simple Python script to create screenshots. Written mostly for demonstration purposes. Dependencies:

* Keyboard
* PyAutoGUI
* Pillow
* Built-in modules (OS, Sys, Datetime)

How this program was built (Russian): https://www.youtube.com/watch?v=rJe_osIzqUY

## How to use it

Run

    python screen.py

Keep the window opened (it does not have to stay in focus) and press "tilda" key to make a PNG screenshot. By default, screenshots are created in the same directory where your script resides, under a `screens` subdirectory.

To provide a custom subdirectory:

    python screen.py my/sub_dir

## Building

To build an executable file you can use `pyinstaller`:

    pyinstaller screen.py

## License

(c) [Ilya Bodrov-Krukowski](http://bodrovis.tech/), licensed under the [beer-ware license](https://fedoraproject.org/wiki/Licensing/Beerware).
