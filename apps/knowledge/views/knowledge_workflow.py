# coding=utf-8

from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema
from rest_framework.request import Request
from rest_framework.views import APIView

from common.auth import TokenAuth
from common.auth.authentication import has_permissions
from common.constants.permission_constants import PermissionConstants, RoleConstants
from common.result import result
from knowledge.api.knowledge_workflow import KnowledgeWorkflowApi
from knowledge.serializers.knowledge_workflow import KnowledgeWorkflowSerializer


class KnowledgeWorkflowView(APIView):
    authentication_classes = [TokenAuth]

    @extend_schema(
        methods=['GET'],
        description=_('Create knowledge workflow'),
        summary=_('Create knowledge workflow'),
        operation_id=_('Create knowledge workflow'),  # type: ignore
        parameters=KnowledgeWorkflowApi.get_parameters(),
        responses=KnowledgeWorkflowApi.get_response(),
        tags=[_('Knowledge Base')]  # type: ignore
    )
    @has_permissions(
        PermissionConstants.KNOWLEDGE_CREATE.get_workspace_permission(),
        RoleConstants.WORKSPACE_MANAGE.get_workspace_role(), RoleConstants.USER.get_workspace_role()
    )
    def post(self, request: Request, workspace_id: str):
        return result.success(KnowledgeWorkflowSerializer.Create(
            data={'user_id': request.user.id, 'workspace_id': workspace_id}
        ).save_workflow(request.data))


class KnowledgeWorkflowVersionView(APIView):
    pass
