from django.shortcuts import render,redirect,get_object_or_404
from django.core.files.storage import FileSystemStorage

from django.http import HttpResponse,HttpResponseBadRequest,FileResponse
from .forms import VideoForm
from .models import Video
from django.conf import settings
import cv2,os

from moviepy.editor import *
from moviepy.editor import VideoFileClip
from PIL import Image

# Create your views here.
# def index(request):
#     all_video=Video.objects.all()
#     if request.method=="POST":
#         form=VideoForm(data=request.POST,files=request.FILES)
#         if form.is_valid():
#             video=form.save()
#             # print(f"\n\n\n\n\n{video}\n\n\n\n\n")
#             new=settings.MEDIA_ROOT + '/' + video.file.path
#             print(new)
#             print(f"\n\n\n\n\n{new}\n\n\n\n\n")
#             # Open the uploaded video file
#             cap = cv2.VideoCapture(settings.MEDIA_ROOT + '/' + video.file.path)
#             # Define the codec and create a video writer
#             fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#             out = cv2.VideoWriter('processed_video.mp4', fourcc, 20.0, (640, 480))
#             # Read each frame of the video
#             while cap.isOpened():
#                 ret, frame = cap.read()
#                 if ret:
#                     # Add the text "Not yet trained" to each frame
#                     cv2.putText(frame, "Not yet trained", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
#                     # Write the processed frame to the output video
#                     out.write(frame)
#                 else:
#                     break
#             # Release the video writer and capture objects
#             out.release()
#             cap.release()

#             return redirect("sidebar.html")
#     else:
#         form=VideoForm()
#     return render(request,'sidebar.html',{"form":form,"all":all_video})


# def index(request):
#     all_video = Video.objects.all()
#     if request.method == "POST":
#         form = VideoForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Uploaded successfully", content_type="text/plain")
#     else:
#         form = VideoForm()
#     return render(request, 'display.html', {"form": form, "all": all_video})




# def index(request):
#     all_video = Video.objects.all()
#     if request.method == "POST":
#         form = VideoForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             # video = form.cleaned_data.get('video')
#             # # video_content = video.read()
#             # video_path = video.temporary_file_path()
#             # print(video_path)
#             # print(video_path)
#             # print(video_path)
#             # print(video_path)
#             # print(video_path)
#             clip = VideoFileClip("media\video\23\VID_37700915_032211_282.mp4").subclip(0, 2)
#             clip2 = VideoFileClip("media\video\23\VID_37700915_032211_282.mp4").subclip(6,10)
#             final_clip = concatenate_videoclips([clip, clip2])
#             final_clip.write_videofile("output_1.mp4")
#             return HttpResponse("Uploaded successfully", content_type="text/plain")
#     else:
#         form = VideoForm()
#     return render(request, 'display.html', {"form": form, "all": all_video})





def index(request):
    all_video = Video.objects.all()
    if request.method == 'POST':
        form = VideoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            video = request.FILES['video']
            fs = FileSystemStorage()
            filename = fs.save(video.name, video)
            video_path = fs.path(filename)

            clip = VideoFileClip(video_path)
            fps = clip.fps
            frame_skip = 50
            frame_count = 0

        # Create a list to store the paths of the saved frames
            frame_paths = []

            for frame in clip.iter_frames():
                if frame_count % frame_skip == 0:
                    frame_file = os.path.join("frame_images1/", f"frame_{frame_count}.png")
                    with open(frame_file, "wb") as f:
                        Image.fromarray(frame).save(f, format='png')
                    frame_paths.append(frame_file)
                frame_count += 1

            clip.reader.close()
            clip.audio.reader.close_proc()

            context = {'frame_paths': frame_paths}
            return render(request, 'sidebar.html', context)

    else:
        form = VideoForm()
    return render(request, 'display.html', {"form": form, "all": all_video})


    # If the request method is not POST, render the upload form
    # return render(request, 'sidebar.html')


# def index(request):
#     all_video = Video.objects.all()
    
#     if request.method == "POST":
#         form = VideoForm(data=request.POST, files=request.FILES)

#         if form.is_valid():
#             form.save()
#             video=form.cleaned_data.get('video')            
#             print(video)
#             print(video)
#             print(video)
#             print(video)
#             print(video)
            
#             # try:
#                 # Open the uploaded video file
#             cap = cv2.VideoCapture('/media/video/23/'+str(video))
#             total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#             arr = []
#             cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
#             _, image = cap.read()
#             out = cv2.VideoWriter('test.mp4',cv2.VideoWriter_fourcc(*'H264'), 
#                                     int(cap.get(cv2.CAP_PROP_FPS)), (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
            
#             for fno in range(total_frames):
#                 cap.set(cv2.CAP_PROP_POS_FRAMES, fno)
#                 _, image = cap.read()
#                 img=cv2.putText(image,"Hello",(255,250),cv2.FONT_ITALIC,1,(255,255,255),3)
#                 out.write(img)
#             out.release()
#             # response = FileResponse(open(str(video), 'rb'))
#             # response['Content-Type'] = 'out/mp4'
#             # response['Content-Disposition'] = 'attachment; filename="modified.mp4"'
#             # return response
            
#             return HttpResponse("Uploaded successfully ", content_type="out")
#     else:
#         form = VideoForm()
#     return render(request, 'sidebar.html', {"form": form, "all": all_video})


def display_video(request):
    video = request.GET.get('video')
    context = {'video': video}
    return render(request, 'display.html', context)