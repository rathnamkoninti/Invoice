from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer
from rest_framework import generics, mixins, status
from rest_framework.response import Response

class InvoiceListCreateView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
    mixins.CreateModelMixin,
):
    serializer_class = InvoiceSerializer

    def get_queryset(self, request):
        queryset = Invoice.objects.filter()
        id = self.request.query_params.get("id", None)
        if id is not None:
            queryset = queryset.filter(pk=id)
        return queryset

    def get(self, request):
        queryset = self.get_queryset(request)
        page_num = int(request.GET.get("page", 1))
        offset = int(request.GET.get("offset", 20))
        start_num = (page_num - 1) * offset
        end_num = offset * page_num
        serializer = self.serializer_class(queryset[start_num:end_num], many=True)
        return Response(
            {
                "status": "Invoice Data",
                "data": serializer.data
            }
        )

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": 201,
                    "message": "Invoice Created Successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"status": 400, "message": "Invoice Create Failed", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
    def put(self, request):
        data=request.data
        try:
            tag_object = Invoice.objects.get(
                id=data.get("id"),
            )
        except:
            return Response(
                {
                    "status": 400,
                    "message": "Invoice Not Found",
                    "data": {},
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.serializer_class(tag_object, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": 200,
                    "message": "Invoice Successfully Updated",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
                {"status": 400, "message": "Invoice Update Failed", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request):
        
        try:
            obj = Invoice.objects.filter(
                id=request.query_params.get("id")
            ).delete()
        except:
            return Response(
                {
                    "status": 400,
                    "message": "Not Found",
                    "data": {},
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {
                "status": 200,
                "message": "Invoice Deleted Successfully",
            },
            status=status.HTTP_200_OK,
        )


class InvoiceDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
    mixins.CreateModelMixin,
):
    serializer_class = InvoiceDetailSerializer

    def get_queryset(self, request,pk):
        queryset = InvoiceDetail.objects.filter(invoice=pk)
        id = self.request.query_params.get("id", None)
        if id is not None:
            queryset = queryset.filter(pk=id)
        return queryset

    def get(self, request,pk):
        queryset = self.get_queryset(request,pk)
        page_num = int(request.GET.get("page", 1))
        offset = int(request.GET.get("offset", 20))
        start_num = (page_num - 1) * offset
        end_num = offset * page_num
        serializer = self.serializer_class(queryset[start_num:end_num], many=True)
        return Response(
            {
                "status": "Invoice Data",
                "data": serializer.data
            }
        )

    def post(self, request,pk):
        data = request.data
        print("data-->154",data)
        data["invoice"]=pk
        print("details--->",data)
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": 201,
                    "message": "InvoiceDetails Created Successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"status": 400, "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
    def put(self, request,pk):
        data=request.data
        try:
            tag_object = InvoiceDetail.objects.get(
                id=data.get("id"),
            )
        except:
            return Response(
                {
                    "status": 400,
                    "message": "Invoice Not Found",
                    "data": {},
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.serializer_class(tag_object, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": 200,
                    "message": "Invoice Successfully Updated",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
                {"status": 400, "message": "Invoice Update Failed", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request,pk):
        
        try:
            obj = InvoiceDetail.objects.filter(
                id=request.data.get("id")
            ).delete()
        except:
            return Response(
                {
                    "status": 400,
                    "message": "Not Found",
                    "data": {},
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {
                "status": 200,
                "message": "Invoice Deleted Successfully",
            },
            status=status.HTTP_200_OK,
        )


# from rest_framework.views import APIView
# class InvoiceListCreateView(APIView):
#     def get_queryset(self, request):
#         queryset = Invoice.objects.filter()
#         id = self.request.query_params.get("id", None)
#         if id is not None:
#             queryset = queryset.filter(id=id)
#         return queryset

#     def get(self, request):
#         topic = self.get_queryset(request)
#         serializer = InvoiceSerializer(topic, many=True)
#         return Response(
#             {
#                 "status": 200,
#                 "message": "Group Data",
#                 "data": serializer.data,
#             },
#             status=status.HTTP_200_OK,
#         )
#     def post(self, request):
        
#         serializer = InvoiceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {
#                     "status": 201,
#                     "message": "Group Created Successfully",
#                     "data": serializer.data,
#                 },
#                 status=status.HTTP_201_CREATED,
#             )
#         return Response(
#             {
#                 "status": 400,
#                 "message": "Failed",
#                 "data": serializer.errors,
#             },
#             status=status.HTTP_400_BAD_REQUEST,
#         )

#     def put(self, request):
#         topic_object = get_object_or_404(Invoice, pk=request.data["id"])
#         serializer = InvoiceSerializer(topic_object, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {
#                     "status": 200,
#                     "message": "Group Details Updated Successfully",
#                     "data": serializer.data,
#                 },
#                 status=status.HTTP_200_OK,
#             )
#         return Response(
#             {"status": 400, "message": serializer.errors, "data": {}},
#             status=status.HTTP_400_BAD_REQUEST,
#         )


#     def delete(self, request):
#         if request.data["role"] == "ADMIN":
#             topic = Invoice.objects.filter(
#                 id=request.query_params.get("id"),
#             ).delete()
#             return Response(
#                 {"status": 200, "message": "Group Deleted Successfully"},
#                 status=status.HTTP_200_OK,
#             )


# class InvoiceDetailView(APIView):
#     def get_queryset(self, request):
#         queryset = InvoiceDetail.objects.filter()
#         id = self.request.query_params.get("id", None)
#         if id is not None:
#             queryset = queryset.filter(id=id)
#         return queryset

#     def get(self, request):
#         article = self.get_queryset(request)
#         serializer = InvoiceDetailSerializer(article, many=True)
#         return Response(
#             {
#                 "status": 200,
#                 "message": "Article Data",
#                 "data": serializer.data,
#             },
#             status=status.HTTP_200_OK,
#         )

#     def post(self, request):
        
#         serializer = InvoiceDetailSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {
#                     "status": 201,
#                     "message": "Invoice Details Created Successfully",
#                     "data": serializer.data,
#                 },
#                 status=status.HTTP_201_CREATED,
#             )
#         else:
#             return Response(
#                 {
#                     "status": 400,
#                     "message": "Fail",
#                     "data": serializer.errors,
#                 },
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
       
#     def put(self, request):
#         article_object = get_object_or_404(InvoiceDetail, pk=request.data["id"])
#         serializer = InvoiceDetailSerializer(
#             article_object, data=request.data, partial=True
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {
#                     "status": 200,
#                     "message": "Article Details Updated Successfully",
#                     "data": serializer.data,
#                 },
#                 status=status.HTTP_200_OK,
#             )
#         return Response(
#             {"status": 400, "message": serializer.errors, "data": {}},
#             status=status.HTTP_400_BAD_REQUEST,
#         )

#     def delete(self, request):
#         article = InvoiceDetail.objects.filter(
#             id=request.query_params.get("id"),
#         ).delte()

#         return Response(
#             {"status": 200, "message": "Article Deleted Successfully"},
#             status=status.HTTP_200_OK,
#         )
