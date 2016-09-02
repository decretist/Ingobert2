# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from ingobert.models import Sample
import diff_match_patch
import re

sourceDict = {'Aa': 'Admont, Stiftsbibliothek 23 and 43',
        'Bc': 'Barcelona, Arxiu de la Corona d\'Aragó, Santa Maria de Ripoll 78',
        '4': 'Vat. lat. 4982',
        '5': 'Beinecke 413, 98r-102r',
        '5bis': 'Beinecke 413, 102v-104v',
        'Sirmond': '1623 Sirmond Edition',
        'Boretius': '1883 Boretius Edition'}

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
    
def demo(request):
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

    template = loader.get_template('ingobert/2column.html')
    context = {
        'page_head': 'Gratian, <cite>Decretum</cite>, D. 63, d.p.c. 34',
        'column_1_head': sourceDict[Aa.source],
        'column_2_head': sourceDict[Bc.source],
        'column_1_body': compare(Aa.text, Bc.text),
        'column_2_body': compare(Bc.text, Aa.text),
    }
    return HttpResponse(template.render(context, request))

