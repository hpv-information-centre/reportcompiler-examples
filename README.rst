Report Compiler examples
########################

This repository will include examples of report specifications to be used with the `Report Compiler`_ library to produce highly customizable documents.

.. _`Report Compiler`: https://github.com/hpv-information-centre/reportcompiler

This project is being developed by the ICO/IARC Information Centre on HPV and Cancer.

.. image:: HPV_infocentre.png
   :height: 50px
   :align: center
   :target: http://www.hpvcentre.net

Report specification examples
=============================
   
example-music
-------------

This report, parameterized with an artist ID, uses the following pipeline:

1. Data fetching: An embedded SQLite database (Chinook_) with data such as artists, albums and tracks (*data* directory)
2. Context generator: A mixture of python and R source files (*src* directory)
3. Template rendering: Jinja2_ to generate a latex document (*templates* directory)
4. Postprocessing: pdflatex to generate a PDF file

Once generated, the output (in *gen/<doc_name>/out*) is a PDF document with a list of the albums and tracks of the specified artist. For example, the following code generates a document with AC/DC (artist id = 1):

.. code:: python

 from reportcompiler.documents import DocumentSpecification

 report_path = '/home/user/reports/example-music'
 report = DocumentSpecification(report_path)
 report.generate({'artist_id': 1})

The report specification can also be obtained via git repository:

.. code:: python

 from reportcompiler.documents import DocumentSpecification

 root_reports_path = '/home/user/reports'
 repo_url = 'https://github.com/hpv-information-centre/reportcompiler-examples'
 report = DocumentSpecification(root_reports_path,
                 repo_url=repo_url,
                 repo_relative_path='example-music')
 report.generate({'artist_id': 1})


.. _Jinja2: http://jinja.pocoo.org/
.. _Chinook: https://github.com/lerocha/chinook-database