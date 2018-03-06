from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class HyPaginator(Paginator):

    @classmethod
    def get_page_data_mobile(cls, curr_page: int, page_num: int, novel_list: list):
        paginator = Paginator(novel_list, page_num)
        try:
            novel_li = paginator.page(curr_page)
        except PageNotAnInteger:
            novel_li = paginator.page(1)
        except EmptyPage:
            novel_li = paginator.page(paginator.num_pages)

        return novel_li

    @classmethod
    def pagination_data(cls, curr_page: int, page_num: int, novel_list: list):

        paginator = Paginator(novel_list, page_num)
        try:
            novel_li = paginator.page(curr_page)
        except PageNotAnInteger:
            novel_li = paginator.page(1)
        except EmptyPage:
            novel_li = paginator.page(paginator.num_pages)

        if curr_page == 1:
            r_num = 6
            l_num = 0
        elif curr_page == 2:
            r_num = 5
            l_num = 1
        elif curr_page == 3:
            r_num = 4
            l_num = 2
        elif curr_page == novel_li.paginator.num_pages:
            l_num = 6
            r_num = 0
        elif curr_page == novel_li.paginator.num_pages - 1:
            l_num = 5
            r_num = 1
        elif curr_page == novel_li.paginator.num_pages - 2:
            l_num = 4
            r_num = 2
        else:
            l_num = 3
            r_num = 3

        l_list = novel_li.paginator.page_range[
            curr_page - l_num - 1 if curr_page - l_num - 1 > 0 else 0: curr_page - 1]
        end_page = curr_page + r_num if curr_page + \
            r_num <= novel_li.paginator.num_pages else novel_li.paginator.num_pages

        r_list = novel_li.paginator.page_range[curr_page: end_page]

        if curr_page + 10 < novel_li.paginator.num_pages:
            next_10 = curr_page + 10
        else:
            next_10 = novel_li.paginator.num_pages
        if curr_page - 10 > 0:
            previous_10 = curr_page - 10
        else:
            previous_10 = 1
        novel_data = {
            "novels": novel_li,
            'l_list': l_list,
            'r_list': r_list,
            'next_10': next_10,
            'previous_10': previous_10
        }
        return novel_data
