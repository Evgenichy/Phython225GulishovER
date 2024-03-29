from .models import Profile, Skill
from django.db.models import Q


def search_profiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains=search_query)  # __iexact точное совпадение

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_info__icontains=search_query) |
        Q(skill_in=skills)
    )

    return profiles, search_query
