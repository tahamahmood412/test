from django.shortcuts import render,HttpResponse
import random
from ExcelDataModel.models import Question,Subject,Chapter


def get_test(request):
    return render(request,"get_test.html")

def shorts_questions(request):
    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        chapter_name = request.POST.get('chapter_name')
        st_questions = int(request.POST.get('amount_of_questions'))
        subject = Subject.objects.get(name=subject_name)
        chapter = Chapter.objects.get(subject=subject, title=chapter_name)
        short_questions = Question.objects.filter(subject=subject, chapter=chapter, question_type='short')
        #Retrieve two random short questions from Chapter 1 of Subject 1
        random_short_questions = random.sample(list(short_questions), min(len(short_questions), st_questions))


        context = {
            'subject': subject,
            'chapter': chapter,
            'st_questions':st_questions,
            'random_short_questions': random_short_questions,
        }
    return render(request, 'short_questions.html', context)