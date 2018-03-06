from math import ceil
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from novels.hy_paginator import HyPaginator
from novels.models import Novel, Chapter
from django.views.generic import ListView

class HomeList(ListView):
    model = Novel

def home_page(request):
    week_hot = Novel.objects.all()[0:3]
    collected_list = Novel.objects.all()[50:60]
    collected_hot = []
    for book in collected_list:
        collected_hot.append({k: str(v).strip()
                              for k, v in model_to_dict(book).items()})

    clicked_list = Novel.objects.all()[20:30]
    clicked_hot = []
    for book in clicked_list:
        clicked_hot.append({k: str(v).strip()
                            for k, v in model_to_dict(book).items()})

    latest_list = Novel.objects.all().order_by('-book_latest')[:10]
    context = {
        'week_hot': week_hot,
        'collected_hot': collected_hot,
        'clicked_hot': clicked_hot,
        'latest_list': latest_list
    }
    return render(request, 'novels/index.html', context)


def novels(request, variety='All', page='1'):
    variety_dic = {
        'XuanHuan': '玄幻小说',
        'QiHuan': '奇幻小说',
        'WuXia': '武侠小说',
        'XianXia': '仙侠小说',
        'DuShi': '都市小说',
        'LiShi': '历史小说',
        'JunShi': '军事小说',
        'YouXi': '游戏小说',
        'JingJi': '竞技小说',
        'LingYi': '灵异小说',
        'KeHuan': '科幻小说',
        'Other': '其他小说',
        'XiuZhen': '修真小说',
        'ChuanYue': '穿越小说',
        'WangYou': '网游小说'
    }
    if variety == 'All':
        novel_list = Novel.objects.all()
    else:
        novel_list = Novel.objects.filter(book_category=variety_dic[variety])

    page_data = HyPaginator.pagination_data(int(page), 20, novel_list)
    context = {
        'page_data': page_data,
        'variety': variety
    }
    return render(request, 'novels/novels.html', context)


def novel_detail(request, novel_id):
    novel = Novel.objects.get(book_identify=novel_id)
    chapter = Chapter.objects.filter(
        book_identify=novel_id).order_by('-chap_identify')[:10]
    correlation = Novel.objects.all().order_by('-book_id')[:8]
    context = {
        'novel': novel,
        'chapter': chapter,
        'correlation': correlation
    }
    return render(request, 'novels/novel_detail.html', context)


def chapter_list(request, novel_id, sort_by, chap_page):
    chap_list = Chapter.objects.filter(book_identify=novel_id)

    if sort_by is None:
        sort_by = "asc"

    if sort_by == "asc":
        chap_list = chap_list.all().order_by('chap_identify')
    else:
        chap_list = chap_list.all().order_by('-chap_identify')

    page_data = HyPaginator.get_page_data_mobile(
        chap_page, page_num=50, novel_list=chap_list)
    novel = Novel.objects.get(book_identify=novel_id)

    page = 0
    curr_page = ''
    page_list = {}
    chap_total = len(chap_list)
    page_total = ceil(chap_total / 50)
    while page < page_total:
        if page + 1 == page_total:
            page_str = '第' + str(page * 50 + 1) + '-' + \
                str(page * 50 + chap_total % 50) + '章'
        else:
            page_str = '第' + str(page * 50 + 1) + '-' + \
                str((page + 1) * 50) + '章'

        page_list[page + 1] = page_str
        if page + 1 == int(chap_page) and sort_by == 'asc':
            curr_page = page_str

        if int(chap_page) == page_total - page and sort_by == 'desc':
            curr_page = page_str

        page += 1

    context = {
        'sort_by': sort_by,
        'page_data': page_data,
        'novel': novel,
        'chap_total': chap_total,
        'page_list': page_list,
        'curr_page': curr_page
    }
    return render(request, 'novels/chapter_list.html', context)


@csrf_protect
def search(request):
    if request.is_ajax():
        kw = request.GET['keyw']
        try:
            # results = Books.objects.get(book_name=kw)
            # data = model_to_dict(results)
            results = Novel.objects.filter(book_name__icontains=kw).values()
            data = {
                "type": 'search',
                "content": list(results)
            }
            return JsonResponse(data)
        except Exception as e:
            return HttpResponse(e)
    else:
        return render(request, 'novels/search.html')
