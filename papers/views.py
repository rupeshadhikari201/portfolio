from django.shortcuts import render
from .models import ResearchPaper

def research_papers(request):
    papers = ResearchPaper.objects.all()
    # Split the authors field into a list of authors
    for paper in papers:
        paper.authors_list = paper.authors.split(",")  # Split authors by comma
    return render(request, 'papers/papers.html', {'papers': papers})
