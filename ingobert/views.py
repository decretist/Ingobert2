# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from ingobert.models import Sample
import diff_match_patch
import re

sourceDict = {
    'Aa': 'Admont, Stiftsbibliothek 23 and 43',
    'Bc': 'Barcelona, Arxiu de la Corona d\'Aragó, Santa Maria de Ripoll 78',
    'Fd': 'Florence, Biblioteca Nazionale Centrale, Conv. Soppr. A. 1.402',
    'P': 'Paris, Bibliothèque Nationale de France, nouvelles acquisitions latines 1761',
    'Pfr': 'Paris, Bibliothèque Nationale de France, latin 3884 I, fo. 1',
}

def compare(left, right):
    a = re.split('[\s\.]+', left.lower())
    b = re.split('[\s\.]+', right.lower())
    column = []
    dmp = diff_match_patch.diff_match_patch()
    (wordText1, wordText2, wordArray) = dmp.diff_linesToChars('\n'.join(a), '\n'.join(b))
    diffs = dmp.diff_main(wordText1, wordText2, False);
    dmp.diff_charsToLines(diffs, wordArray)
    for diff in diffs:
        text = ' '.join(re.split('\n', diff[1]))
        if diff[0] == 1:
            continue
        elif diff[0] == 0:
            column.append(text)
        elif diff[0] == -1:
            column.append('<span class=highlight>' + text.rstrip() + '</span>')
    return(' '.join(column))
    
def load(request):
    samples = Sample.objects.all()
    for sample in samples:
        sample.delete()

    Aa = Sample()
    Aa.project = 102
    Aa.source = 'Aa'
    Aa.label = 'D.63 d.p.c.34'
    Aa.text = '''Nunc autem sicut electio summi pontificis non a cardinalibus tantum immo etiam ab aliis religiosis clericis auctoritate Nicholai papȩ est facienda ita et episcoporum electio non a canonicis tantum set etiam ab aliis religiosis clericis sicut in generali synodo Innocentii papȩ romȩ habita constitutum est.'''
    Aa.save() 

    Bc = Sample()
    Bc.project = 102
    Bc.source = 'Bc'
    Bc.label = 'D.63 d.p.c.34'
    Bc.text = '''Nunc autem sicut electio summi pontificis non a cardinalibus tantum immo etiam ab aliis religiosis clericis auctoritate nicholay pape est facienda ita et episcoporum electio non a canonicis tantum set etiam ab aliis religiosis clericis sicut in generali synodo innocentii pape rome habita constitutum est.'''
    Bc.save()

    return HttpResponse('load')

def demo(request):
    Aa = Bc = Sample()
    label = 'D.63 d.p.c.34'
    project_name = 'Decretum Gratiani'
    samples = Sample.objects.filter(project = 102).filter(label__exact = label)
    for sample in samples:
        if sample.source == 'Aa':
            Aa = sample
        elif sample.source == 'Bc':
            Bc = sample
    template = loader.get_template('ingobert/2column.html')
    context = {
        'page_head': '<cite>' + project_name + '</cite>, ' + label,
        'column_1_head': sourceDict[Aa.source],
        'column_2_head': sourceDict[Bc.source],
        'column_1_body': compare(Aa.text, Bc.text),
        'column_2_body': compare(Bc.text, Aa.text),
    }
    return HttpResponse(template.render(context, request))

