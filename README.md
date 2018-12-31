# Ingobert2-etc

(30 December 2018)

- [ ] Merge Ingobert2 and Ingobert2-etc repositories
---
`load1.xml` is a handcrafted data fixture in django-objects XML
format that I created during the earliest stages (September 2016?)
of porting the Ingobert app from the Google App Engine (GAE) platform
to Django.

`load1.xml` encodes variant readings of D.63 d.p.c.34 from the Aa
and Bc manuscripts of Gratian's _Decretum_.

---
`upload.xml` is the final version of the original XML upload file
for the GAE bulkloader. (c.2010-14.) It is identical to
`Ingobert/etc/upload.xml`.

`treewalk.py` is an early (October 2016) experiment in XML parsing.
It reads upload.xml, transforms the data from GAE bulkloader to
plain text format, and prints the resulting text to standard output:

`treebuild2.py` reads `upload.xml`, transforms the data from GAE
bulkloader to django-objects format, and prints the resulting XML
to standard output:

`./treebuild2.py > load2.xml`.

`load2.xml` encodes variant readings of the Capitulare Carisiacense
(873) from Beinecke MS 413.

---
`Samples.py` is a Python module containing a list of dictionaries
encoding variant readings of the case statements (_themata_) from
the Sg manuscript, first recension, and 1879 Friedberg edition of
Gratian's _Decretum_:
```python
listofdicts = [
  {
    'project': 'Gratian',
    'source': 'Fr.',
    'label': 'C. 1, d.init.',
    'text': '''Quidam habens filium obtulit eum ditissimo cenobio ...'''
  },
  {
    'project': 'Gratian',
    'source': 'Sg',
    'label': 'C. 1, d.init.',
    'text': '''Obtulit quidam filium suum cenobio ...'''
  },
  ...
]
```
**In future, all changes to data fixtures are to be made by adding a
dictionary entry to `Samples.py`!**

`treebuild3.py` imports `Samples.py`, transforms the data into
django-objects format, and prints the resulting XML to standard
output:

`./treebuild3.py > load3.xml`.

To replicate the checked-in version of `load3.xml`, comment out
lines 30-34 of `treebuild3.py`:
```python
text = text.replace('cia', 'tia')
text = text.replace('cio', 'tio')
text = text.replace('ae', 'e')
text = text.replace('V', 'U')
text = text.replace('v', 'u')
```
`load3.xml` is an XML representation in django-objects format of
the case statements in Gratian's _Decretum_ derived from `Samples.py`:
```xml
<django-objects version="1.0">
  <object model="ingobert.sample">
    <field name="project" type="CharField">Gratian</field>
    <field name="source" type="CharField">Fr.</field>
    <field name="label" type="CharField">C. 1, d.init.</field>
    <field name="text" type="TextField">quidam habens filium obtulit eum ditissimo cenobio ...</field>
  </object>
  <object model="ingobert.sample">
    <field name="project" type="CharField">Gratian</field>
    <field name="source" type="CharField">Sg</field>
    <field name="label" type="CharField">C. 1, d.init.</field>
    <field name="text" type="TextField">obtulit quidam filium suum cenobio ...</field>
  </object>
  ...
</django-objects>
```
---
The final Django data fixture is created by concatenating `load1.xml`,
`load2.xml`, and `load3.xml`, in that order, into a single file,
then hand-editing the resulting file to make sure that there is
only one pair of django-objects start and end tags:
```xml
<django-objects version="1.0">
  ...
</django-objects>
```
---
## Files

```
-r--r--r-- 1 ple staff 7 2016-11-27T21:00:00 .gitignore
-r--r--r-- 1 ple staff 15 2016-11-27T21:00:00 README.md
-r-xr-xr-x 1 ple staff 1497 2016-11-27T20:43:00 treebuild3.py
-r--r--r-- 1 ple staff 59027 2016-11-26T20:48:07 load2.xml
-r--r--r-- 1 ple staff 1264 2016-11-26T19:52:43 load1.xml
-r-xr-xr-x 1 ple staff 1442 2016-11-26T19:29:15 treebuild2.py
-r--r--r-- 1 ple staff 100385 2016-11-13T20:23:12 load3.xml
-r-xr-xr-x 1 ple staff 85654 2016-11-13T20:23:00 Samples.py
-r-xr-xr-x 1 ple staff 457 2016-10-17T19:09:35 treewalk.py
-r--r--r-- 1 ple staff 53901 2014-12-15T08:08:56 upload.xml
```

