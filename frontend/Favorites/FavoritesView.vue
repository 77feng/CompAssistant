<!-- frontend/src/components/FavoritesView.vue -->
<template>
  <div class="favorites-view">
    <h2>❤️ 我的收藏</h2>
    <div v-if="favoriteComps.length === 0" class="empty">
      <p>暂无收藏的竞赛，去竞赛列表添加吧～</p>
    </div>
    <div v-else class="competitions-grid">
      <div
        v-for="comp in favoriteComps"
        :key="comp.id"
        class="competition-card"
        @click="viewDetail(comp)"
      >
        <div class="card-header">
          <h3 class="competition-name">{{ comp.name }}</h3>
          <span :class="['difficulty-badge', comp.difficulty?.toLowerCase()]">
            {{ comp.difficulty }}
          </span>
        </div>
        <div class="card-content">
          <div class="info-item">
            <span class="label">截止时间</span>
            <span class="value deadline">{{ formatDate(comp.deadline) }}</span>
          </div>
          <div class="info-item">
            <span class="label">竞赛领域</span>
            <span class="value">{{ comp.field }}</span>
          </div>
        </div>
        <div class="card-footer">
          <span :class="['days-left', { expired: isExpired(comp.deadline) }]">
            {{ getStatusText(comp.deadline) }}
          </span>
        </div>
      </div>
    </div>

    <!-- 详情模态框（简化版，可复用 CompetitionList 的样式） -->
    <div v-if="selectedComp" class="modal-overlay" @click="selectedComp = null">
      <div class="modal-content" @click.stop>
        <button class="close-btn" @click="selectedComp = null">✕</button>
        <div class="modal-header">
          <h2>{{ selectedComp.name }}</h2>
          <span :class="['difficulty-badge', selectedComp.difficulty?.toLowerCase()]">
            {{ selectedComp.difficulty }}
          </span>
        </div>
        <div class="modal-body">
          <p><strong>简介</strong>：{{ selectedComp.description }}</p>
          <p v-if="selectedComp.links?.length">
            <strong>官网</strong>：
            <a :href="selectedComp.links[0].url" target="_blank" rel="noopener noreferrer">
              {{ selectedComp.links[0].name }} ↗
            </a>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import { useFavorites } from '../composables/useFavorites'

export default {
  name: 'FavoritesView',
  setup() {
    const allCompetitions = ref([])
    const selectedComp = ref(null)
    const { favoriteIds } = useFavorites()

    const fetchAll = async () => {
      try {
        const res = await axios.get('/api/competitions')
        allCompetitions.value = res.data
      } catch (e) {
        console.error('获取竞赛列表失败', e)
      }
    }

    onMounted(fetchAll)

    const favoriteComps = computed(() => {
      return allCompetitions.value.filter(c => favoriteIds.value.has(c.id))
    })

    const formatDate = (dateStr) => {
      if (!dateStr) return '待定'
      const date = new Date(dateStr)
      return date.toLocaleString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
      })
    }

    const getDaysRemaining = (deadline) => {
      if (!deadline) return Infinity
      return Math.ceil((new Date(deadline) - new Date()) / (1000 * 60 * 60 * 24))
    }

    const getStatusText = (deadline) => {
      const days = getDaysRemaining(deadline)
      if (days < 0) return '已截止'
      if (days === 0) return '今天截止'
      return `${days} 天`
    }

    const isExpired = (deadline) => getDaysRemaining(deadline) < 0
    const viewDetail = (comp) => { selectedComp.value = comp }

    return {
      favoriteComps,
      selectedComp,
      formatDate,
      getStatusText,
      isExpired,
      viewDetail
    }
  }
}
</script>

<style scoped>
.favorites-view {
  padding: 24px;
  background-color: #ffffff;
  min-height: 100%;
}
.favorites-view h2 {
  font-size: 28px;
  font-weight: 700;
  margin-bottom: 24px;
}
.empty {
  text-align: center;
  margin-top: 80px;
  color: #86868b;
  font-size: 16px;
}
.competitions-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 16px;
}
.competition-card {
  background-color: #ffffff;
  border: 1px solid #d2d2d7;
  border-radius: 12px;
  padding: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
}
.competition-card:hover {
  border-color: #0071e3;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
}
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 12px;
}
.competition-name {
  font-size: 16px;
  font-weight: 600;
  flex: 1;
  margin-right: 8px;
}
.difficulty-badge {
  padding: 4px 8px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
}
.difficulty-badge.简单 { background-color: #e8f5e9; color: #2e7d32; }
.difficulty-badge.中等 { background-color: #fff3e0; color: #e65100; }
.difficulty-badge.困难 { background-color: #ffebee; color: #c62828; }
.card-content {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 12px;
}
.info-item {
  display: flex;
  justify-content: space-between;
  font-size: 13px;
}
.info-item .label { color: #86868b; }
.info-item .value { color: #1d1d1f; font-weight: 500; }
.deadline { color: #0071e3; }
.card-footer {
  padding-top: 12px;
  border-top: 1px solid #f5f5f7;
}
.days-left { font-size: 14px; font-weight: 600; color: #0071e3; }
.days-left.expired { color: #86868b; }
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}
.modal-content {
  background-color: #ffffff;
  border-radius: 16px;
  max-width: 500px;
  width: 90%;
  max-height: 80vh;
  overflow-y: auto;
  position: relative;
  padding: 20px;
}
.close-btn {
  position: absolute;
  top: 12px;
  right: 12px;
  background: #f5f5f7;
  border: none;
  border-radius: 50%;
  width: 32px;
  height: 32px;
  cursor: pointer;
  font-size: 18px;
}
.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
  padding-right: 24px;
}
.modal-body p {
  margin: 12px 0;
  line-height: 1.5;
}
</style>