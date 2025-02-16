from django.shortcuts import render
from django.db.models import F
from rest_framework import viewsets
from .models import Question, Solution, Keypoint, Category
from .serializers import QuestionSerializer, SolutionSerializer, KeypointSerializer, CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = Question.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset

class SolutionViewSet(viewsets.ModelViewSet):
    serializer_class = SolutionSerializer

    def get_queryset(self):
        queryset = Solution.objects.all().annotate(question_name=F('question__name'))
        category = self.request.query_params.get('category', None)
        keypoint = self.request.query_params.get('keypoint', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        if keypoint is not None:
            queryset = queryset.filter(keypoint=keypoint)
        return queryset

class KeypointViewSet(viewsets.ModelViewSet):
    serializer_class = KeypointSerializer

    def get_queryset(self):
        queryset = Keypoint.objects.all()
        return queryset
