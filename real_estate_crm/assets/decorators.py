# # decorators.py

# from django.conf import settings
# from django.http import JsonResponse
# from functools import wraps

# def api_key_required(view_func):
#     @wraps(view_func)
#     def _wrapped_view(request, *args, **kwargs):
#         api_key = request.headers.get('API-Key')
#         if api_key != settings.SIMPLE_API_KEY:
#             return JsonResponse({'error': 'Unauthorized'}, status=401)
#         return view_func(request, *args, **kwargs)
#     return _wrapped_view
