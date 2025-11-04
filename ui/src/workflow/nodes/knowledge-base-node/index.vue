<template>
  <NodeContainer :nodeModel="nodeModel">
    <UserInputFieldTable ref="UserInputFieldTableFef" :node-model="nodeModel" />
  </NodeContainer>
</template>
<script setup lang="ts">
import { set } from 'lodash'
import NodeContainer from '@/workflow/common/NodeContainer.vue'
import type { FormInstance } from 'element-plus'
import { ref, computed, onMounted, inject } from 'vue'
import { t } from '@/locales'
import UserInputFieldTable from './component/UserInputFieldTable.vue'

const getResourceDetail = inject('getResourceDetail') as any

const props = defineProps<{ nodeModel: any }>()

const UserInputFieldTableFef = ref()

const baseNodeFormRef = ref<FormInstance>()

const resource = getResourceDetail()

onMounted(() => {})
</script>
<style lang="scss" scoped>
:deep(.el-form-item__label) {
  display: block;
}
</style>
