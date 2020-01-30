from django.shortcuts import render
from .apps import PredictorConfig
from django.http import JsonResponse
from rest_framework.views import APIView
import numpy as np
class call_model(APIView):
    def get(self,request):
        if request.method == 'GET':

            caller_id = request.GET.get('caller_id')
            location = request.GET.get('location')
            resolved_by = request.GET.get('resolved_by')
            opened_by = request.GET.get('opened_by')

            vector = np.array([caller_id, location, resolved_by, opened_by])
            vector = vector.reshape(1,-1)
            prediction = PredictorConfig.randomForest.predict(vector)[0]
            prediction2 = PredictorConfig.decisionTree.predict(vector)[0]
            average = (prediction + prediction2) / 2

            response = {'Random Forest Regressor': prediction,
                        'Decision Tree:': prediction2,
                        'Valeur probable': average}

            return JsonResponse(response)