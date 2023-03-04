import requests
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import permissions
from django.shortcuts import render
from django.conf import settings
# from django.views.generic import TemplateView

def index(request):
    return render(request, "index.html")

class StableDiffusionTestAPIView(APIView):
    permission_classes = [permissions.AllowAny,]
    
    def post(self, request, *args, **kwargs):
        data = request.data
        prompt = data['prompt']
        # init_image = data["init_image"]
        end_point = 'https://stablediffusionapi.com/api/v3/text2img'
        # data = {
        #     "key": settings.STABLE_DIFFUSION_API_KEY,
        #     "prompt": prompt,
        #     # "negative_prompt": null,
        #     # "init_image": init_image,
        #     "width": "512",
        #     "height": "512",
        #     "samples": "1",
        #     "num_inference_steps": "30",
        #     "guidance_scale": 7.5,
        #     "safety_checker":"yes",
        #     "strength": 0.7,
        #     # "seed": null,
        #     # "webhook": null,
        #     # "track_id": null
        # }

        data = {
            "key": settings.STABLE_DIFFUSION_API_KEY,
            "prompt": prompt,
            #  "negative_prompt": "((out of frame)), ((extra fingers)), mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), (((tiling))), ((naked)), ((tile)), ((fleshpile)), ((ugly)), (((abstract))), blurry, ((bad anatomy)), ((bad proportions)), ((extra limbs)), cloned face, (((skinny))), glitchy, ((extra breasts)), ((double torso)), ((extra arms)), ((extra hands)), ((mangled fingers)), ((missing breasts)), (missing lips), ((ugly face)), ((fat)), ((extra legs)), anime",
            "width": "512",
            "height": "512",
            "samples": "1",
            "num_inference_steps": "20",
            #  "seed": null,
            "guidance_scale": 7.5,
            "safety_checker":"yes",
            #  "webhook": null,
            #  "track_id": null
        }

        response = requests.post(end_point, data=data)
        if response.status_code == 200:
            response_data = response.json()
            try:
                outputs = response_data['output']
                return Response(outputs)
            except KeyError:
                print(response_data)
                return Response({"message": response_data['message']}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "fail"}, status=status.HTTP_400_BAD_REQUEST)
    

# class StableDiffusionTestTemplateView(TemplateView):
#     template_name = ""