# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from ingobert.models import Sample
from . import diff_match_patch
import difflib
import re

sourceDict = {
    'Aa': 'Admont, Stiftsbibliothek 23 and 43',
    'Bc': 'Barcelona, Arxiu de la Corona d\'Aragó, Santa Maria de Ripoll 78',
    'Fd': 'Florence, Biblioteca Nazionale Centrale, Conv. Soppr. A. 1.402',
    'P': 'Paris, Bibliothèque Nationale de France, nouvelles acquisitions latines 1761',
    'Pfr': 'Paris, Bibliothèque Nationale de France, latin 3884 I, fo. 1',
    '4': 'Vat. lat. 4982',
    '5': 'Beinecke 413, 98r-102r',
    '5bis': 'Beinecke 413, 102v-104v',
    'Sirmond': '1623 Sirmond Edition',
    'Boretius': '1883 Boretius Edition'
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
    
def contrast(left, right):
    a = re.split('[\s\.]+', left.lower())
    b = re.split('[\s\.]+', right.lower())
    column = []
    diffs = difflib.ndiff(a, b)
    for diff in diffs:
        if re.match('  $', diff):
            continue
        elif re.match('\? ', diff):
            continue
        elif re.match('- ', diff):
            column.append('<span class=highlight>' + str.replace(diff, '- ', '') + '</span>')
        elif re.match('\+ ', diff):
            pass
        else:
            column.append(str.replace(diff, '  ', ''))
    return ' '.join(column)

def demo(request):
    Aa = Bc = Sample()
    label = 'D. 63, d.p.c. 34'
    project = 'Gratian, <cite>Decretum</cite>'
    page_head = project + ', ' + label
    samples = Sample.objects.filter(project = 'Gratian').filter(label__exact = label)
    for sample in samples:
        if sample.source == 'Aa':
            Aa = sample
        elif sample.source == 'Bc':
            Bc = sample
    template = loader.get_template('ingobert/2column.html')
    context = {
        'page_head': page_head,
        'column_1_head': sourceDict[Aa.source],
        'column_2_head': sourceDict[Bc.source],
        'column_1_body': contrast(Aa.text, Bc.text),
        'column_2_body': contrast(Bc.text, Aa.text),
    }
    return HttpResponse(template.render(context, request))

def two_column(request):
    if request.method == 'POST':
        project = request.POST.get('project', '')
        label = request.POST.get('label', '')
        if (project == 'Gratian'):
            page_head = 'Gratian, <cite>Decretum</cite>, ' + label
        else:
            page_head = project + ', ' + label
        samples = Sample.objects.filter(project__exact = project).filter(label__exact = label)
        column_1 = column_2 = None
        column_1_body = column_2_body = ''
        for sample in samples:
            if (sample.source == request.POST.get('column_1', '')):
                column_1 = sample
            if (sample.source == request.POST.get('column_2', '')):
                column_2 = sample
        if column_1 is not None:
            if column_2 is not None:
                column_1_body = contrast(column_1.text, column_2.text)
            else:
                column_1_body = contrast(column_1.text, '')
        if column_2 is not None:
            if column_1 is not None:
                column_2_body = contrast(column_2.text, column_1.text)
            else:
                column_2_body = contrast(column_2.text, '')
        template = loader.get_template('ingobert/2column.html')
        context = {
            'page_head': page_head,
            'column_1_head': sourceDict[request.POST.get('column_1', '')],
            'column_2_head': sourceDict[request.POST.get('column_2', '')],
            'column_1_body': column_1_body,
            'column_2_body': column_2_body,
        }
        return HttpResponse(template.render(context, request))
    # GET works, but generates hideous URLs
    elif request.method == 'GET':
        project = request.GET.get('project', '')
        label = request.GET.get('label', '')
        column_1 = request.GET.get('column_1', '')
        column_2 = request.GET.get('column_2', '')
        response = 'GET' + ' ' + project + ' ' + label + ' ' + column_1 + ' ' + column_2
        return HttpResponse(response)
    else:
        return HttpResponse('unknown')

def four_column(request):
    if request.method == 'POST':
        project = request.POST.get('project', '')
        label = request.POST.get('label', '')
        title = project + ', ' + label
        samples = Sample.objects.filter(project__exact = project).filter(label__exact = label)
        tmps = [None, None, None, None]
        sourceList = ['5', '5bis', 'Sirmond', 'Boretius']
        sourceList.remove(request.POST.get('comparison', ''))
        for sample in samples:
            if (sample.source == request.POST.get('comparison', '')):
                tmps[0] = sample
            if (sample.source == sourceList[0]):
                tmps[1] = sample
            if (sample.source == sourceList[1]):
                tmps[2] = sample
            if (sample.source == sourceList[2]):
                tmps[3] = sample
        columns = []
        for tmp in tmps:
            column = {}
            if (tmp != None):
                if (tmp == tmps[0]):
                    column['highlight'] = True
                column['source'] = sourceDict[tmp.source]
                if (tmps[0] != None):
                    column['text'] = contrast(tmp.text, tmps[0].text)
                elif (tmps[0] == None):
                    column['text'] = contrast(tmp.text, '')
            columns.append(column)
        template = loader.get_template('ingobert/4column.html')
        context = {
            'title': title,
            'columns': columns,
        }
        return HttpResponse(template.render(context, request))

def home(request):
    context = {}
    template = loader.get_template('ingobert/home.html')
    return HttpResponse(template.render(context, request))

