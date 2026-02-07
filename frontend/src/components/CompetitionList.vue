<template>
  <div class="competition-list">
    <!-- 顶部筛选栏 -->
    <div class="filter-bar">
      <div class="search-box">
        <input 
          v-model="searchQuery"
          type="text" 
          placeholder="搜索竞赛..."
          class="search-input"
          @input="filterCompetitions"
        />
        <span class="search-icon">🔍</span>
      </div>

      <div class="filters">
        <div class="filter-group">
          <label>竞赛领域</label>
          <select v-model="selectedField" @change="filterCompetitions" class="filter-select">
            <option value="">全部领域</option>
            <option value="人工智能">人工智能</option>
            <option value="算法/编程">算法/编程</option>
            <option value="Web开发">Web开发</option>
            <option value="移动开发">移动开发</option>
            <option value="数据科学">数据科学</option>
            <option value="数学/建模">数学/建模</option>
            <option value="硬件/电子">硬件/电子</option>
            <option value="硬件/芯片">硬件/芯片</option>
            <option value="机器人/智能车">机器人/智能车</option>
            <option value="网络安全">网络安全</option>
            <option value="游戏开发">游戏开发</option>
            <option value="综合/创新创业">综合/创新创业</option>
            <option value="综合/科技">综合/科技</option>
            <option value="英语/语言">英语/语言</option>
            <option value="设计/应用">设计/应用</option>
            <option value="其他">其他</option>
          </select>
        </div>

        <div class="filter-group">
          <label>竞赛级别</label>
          <select v-model="selectedLevel" @change="filterCompetitions" class="filter-select">
            <option value="">全部级别</option>
            <option value="S">S级</option>
            <option value="A+">A+级</option>
            <option value="A">A级</option>
            <option value="B+">B+级</option>
            <option value="B">B级</option>
          </select>
        </div>
      </div>
    </div>

    <!-- 竞赛列表 -->
    <div class="competitions-container">
      <div v-if="loading" class="loading">
        <p>加载中...</p>
      </div>
      <div v-else-if="errorMsg" class="error-container">
        <p class="error-text">{{ errorMsg }}</p>
        <button @click="fetchCompetitions" class="retry-btn">重试</button>
      </div>
      <div v-else-if="filteredCompetitions.length === 0" class="no-data">
        <p>暂无符合条件的竞赛</p>
      </div>

      <div v-else class="competitions-grid">
        <div 
          v-for="competition in filteredCompetitions" 
          :key="competition.id"
          :class="['competition-card', { expired: isExpiredForView(competition.deadline) }]"
          @click="selectCompetition(competition)"
        >
          <div class="card-header">
            <h3 class="competition-name">{{ competition.name }}</h3>
            <span :class="['difficulty-badge', competition.difficulty ? competition.difficulty.toLowerCase() : '']">
              {{ competition.difficulty }}
            </span>
          </div>

          <div class="card-content">
            <div class="info-item">
              <span class="label">截止时间</span>
              <span class="value deadline">{{ formatDate(competition.deadline) }}</span>
            </div>
            <div class="info-item">
              <span class="label">竞赛领域</span>
              <span class="value">{{ competition.field }}</span>
            </div>
            <div class="info-item">
              <span class="label">竞赛难度</span>
              <span class="value">{{ competition.difficulty }}</span>
            </div>
            <div class="info-item">
              <span class="label">竞赛级别</span>
              <span :class="['value', 'level', competition.level]">
                {{ competition.level }}
              </span>
            </div>
          </div>

          <div class="card-footer">
            <span :class="['days-left', { expired: isExpiredForView(competition.deadline) }]">
              {{ getStatusText(competition.deadline) }}
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- 竞赛详情模态框 -->
    <div v-if="selectedCompetition" class="modal-overlay" @click="closeModal">
      <div class="modal-content" @click.stop>
        <button class="close-btn" @click="closeModal">✕</button>

        <div class="modal-header">
          <h2>{{ selectedCompetition.name }}</h2>
          <span :class="['difficulty-badge', selectedCompetition.difficulty ? selectedCompetition.difficulty.toLowerCase() : '']">
            {{ selectedCompetition.difficulty }}
          </span>
        </div>

        <div class="modal-body">
          <section class="detail-section">
            <h4>基本信息</h4>
            <div class="detail-grid">
              <div class="detail-item">
                <span class="detail-label">截止时间</span>
                <span class="detail-value">{{ formatDate(selectedCompetition.deadline) }}</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">当前状态</span>
                <span
                  :class="[
                    'detail-value',
                    getStatusInfo(selectedCompetition.deadline).expired
                      ? 'status-expired'
                      : 'status-active'
                  ]"
                >
                  {{ getStatusInfo(selectedCompetition.deadline).label }}
                </span>
              </div>
              <div class="detail-item">
                <span class="detail-label">竞赛领域</span>
                <span class="detail-value">{{ selectedCompetition.field }}</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">竞赛级别</span>
                <span class="detail-value">{{ selectedCompetition.level }}</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">难度等级</span>
                <span class="detail-value">{{ selectedCompetition.difficulty }}</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">官网链接</span>
                <span class="detail-value">
                  <a
                    v-if="getOfficialLink(selectedCompetition)"
                    :href="getOfficialLink(selectedCompetition).url"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    {{ getOfficialLink(selectedCompetition).name }} ↗
                  </a>
                  <span v-else>—</span>
                </span>
              </div>
            </div>
          </section>

          <section class="detail-section">
            <h4>竞赛简介</h4>
            <p>{{ selectedCompetition.description }}</p>
          </section>

          <section v-if="selectedCompetition.suggestions && selectedCompetition.suggestions.length > 0" class="detail-section">
            <h4>参赛建议</h4>
            <ul class="suggestions-list">
              <li v-for="(suggestion, index) in selectedCompetition.suggestions" :key="index">
                {{ suggestion }}
              </li>
            </ul>
          </section>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'

export default {
  name: 'CompetitionList',
  setup() {
    const searchQuery = ref('')
    const selectedField = ref('')
    const selectedLevel = ref('')
    const selectedCompetition = ref(null)
    const competitions = ref([])
    const loading = ref(true)
    const errorMsg = ref('')

    // 从后端获取数据
    const fetchCompetitions = async () => {
      try {
        loading.value = true
        errorMsg.value = ''
        // 确保代理已配置或直接指向后端地址
        const response = await axios.get('/api/competitions')
        competitions.value = response.data
      } catch (error) {
        console.error('Error fetching competitions:', error)
        errorMsg.value = '无法连接到服务器，请确保后端已启动'
      } finally {
        loading.value = false
      }
    }

    onMounted(() => {
      fetchCompetitions()
    })

    const filteredCompetitions = computed(() => {
      return competitions.value.filter(comp => {
        const matchesSearch = comp.name.toLowerCase().includes(searchQuery.value.toLowerCase())
        // 后端field可能为null，需要处理
        const matchesField = !selectedField.value || (comp.field && comp.field === selectedField.value)
        const matchesLevel = !selectedLevel.value || (comp.level && comp.level === selectedLevel.value)
        return matchesSearch && matchesField && matchesLevel
      })
    })

    const filterCompetitions = () => {
      // 过滤逻辑已在computed属性中实现
    }

    const formatDate = (dateStr) => {
      if (!dateStr) return '待定'
      const date = new Date(dateStr)
      return date.toLocaleString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: false
      })
    }

    const getStatusInfo = (deadline) => {
      if (!deadline) {
        return { label: '待定', expired: false }
      }
      const now = new Date()
      const deadlineDate = new Date(deadline)
      const currentYear = now.getFullYear()
      const deadlineYear = deadlineDate.getFullYear()

      if (deadlineYear < currentYear) {
        return { label: '未开始', expired: false }
      }

      if (deadlineYear === currentYear && deadlineDate < now) {
        return { label: '已截止', expired: true }
      }

      const diffTime = deadlineDate - now
      const diffDays = Math.max(0, Math.ceil(diffTime / (1000 * 60 * 60 * 24)))
      return { label: `${diffDays} 天`, expired: false }
    }

    const getStatusText = (deadline) => getStatusInfo(deadline).label

    const isExpiredForView = (deadline) => getStatusInfo(deadline).expired

    const selectCompetition = (competition) => {
      selectedCompetition.value = competition
    }

    const closeModal = () => {
      selectedCompetition.value = null
    }

    const getOfficialLink = (competition) => {
      if (!competition || !competition.links || competition.links.length === 0) return null
      return competition.links.find(link => link.name === '赛事官网') || competition.links[0]
    }

    return {
      searchQuery,
      selectedField,
      selectedLevel,
      filteredCompetitions,
      selectedCompetition,
      filterCompetitions,
      formatDate,
      getStatusInfo,
      getStatusText,
      isExpiredForView,
      selectCompetition,
      closeModal,
      getOfficialLink,
      loading,
      errorMsg,
      fetchCompetitions
    }
  }
}
</script>

<style scoped>
.competition-list {
  display: flex;
  flex-direction: column;
  height: 100%;
  overflow: hidden;
}

/* 筛选栏 */
.filter-bar {
  padding: 24px;
  border-bottom: 1px solid #d2d2d7;
  background-color: #ffffff;
  display: flex;
  gap: 16px;
  align-items: flex-end;
  flex-wrap: wrap;
}

.search-box {
  flex: 1;
  min-width: 300px;
  position: relative;
}

.search-box label {
  display: block;
  font-size: 13px;
  font-weight: 600;
  color: #86868b;
  margin-bottom: 6px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.search-input {
  width: 100%;
  padding: 10px 40px 10px 14px;
  border: 1px solid #d2d2d7;
  border-radius: 8px;
  font-size: 15px;
  background-color: #f5f5f7;
  transition: all 0.2s ease;
}

.search-input:focus {
  outline: none;
  background-color: #ffffff;
  border-color: #0071e3;
  box-shadow: 0 0 0 3px rgba(0, 113, 227, 0.1);
}

.search-icon {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: #86868b;
  pointer-events: none;
  margin-top: 8px;
}

.filters {
  display: flex;
  gap: 16px;
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.filter-group label {
  font-size: 13px;
  font-weight: 600;
  color: #86868b;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.filter-select {
  padding: 10px 14px;
  border: 1px solid #d2d2d7;
  border-radius: 8px;
  font-size: 15px;
  background-color: #f5f5f7;
  cursor: pointer;
  transition: all 0.2s ease;
  color: #1d1d1f;
}

.filter-select:hover {
  border-color: #a1a1a6;
}

.filter-select:focus {
  outline: none;
  background-color: #ffffff;
  border-color: #0071e3;
}

/* 竞赛容器 */
.competitions-container {
  flex: 1;
  overflow-y: auto;
  padding: 24px;
  background-color: #ffffff;
}

.no-data {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  color: #86868b;
  font-size: 16px;
}

.competitions-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 16px;
}

/* 竞赛卡片 */
.competition-card {
  background-color: #ffffff;
  border: 1px solid #d2d2d7;
  border-radius: 12px;
  padding: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
}

.competition-card:hover {
  border-color: #0071e3;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
  transform: translateY(-2px);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 12px;
  gap: 8px;
}

.competition-name {
  font-size: 16px;
  font-weight: 600;
  color: #1d1d1f;
  flex: 1;
  line-height: 1.4;
}

.difficulty-badge {
  padding: 4px 8px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
}

.difficulty-badge.简单 {
  background-color: #e8f5e9;
  color: #2e7d32;
}

.difficulty-badge.中等 {
  background-color: #fff3e0;
  color: #e65100;
}

.difficulty-badge.困难 {
  background-color: #ffebee;
  color: #c62828;
}

.card-content {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 12px;
  flex: 1;
}

.info-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 13px;
}

.info-item .label {
  color: #86868b;
  font-weight: 500;
}

.info-item .value {
  color: #1d1d1f;
  font-weight: 500;
}

.deadline {
  color: #0071e3;
  font-family: monospace; /* 更加适合显示时间 */
}

.level.S {
  color: #c62828;
  font-weight: 700;
}

.level.A\+ {
  color: #e65100;
}

.level.A {
  color: #f57f17;
}

.level.B\+ {
  color: #2e7d32;
}

.level.B {
  color: #1565c0;
}

.level.other {
  color: #86868b;
}

.card-footer {
  padding-top: 12px;
  border-top: 1px solid #f5f5f7;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.days-left {
  font-size: 14px;
  font-weight: 600;
  color: #0071e3;
}

.days-left.expired {
  color: #86868b;
  font-weight: 500;
}

.competition-card.expired {
  background-color: #fafafa;
  border-color: #e8e8ed;
}

.competition-card.expired .competition-name {
  color: #666;
}

.status-expired {
  color: #86868b;
  font-weight: 600;
}

.status-active {
  color: #0071e3;
  font-weight: 600;
}

.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 200px;
  font-size: 16px;
  color: #86868b;
}

.error-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 200px;
  gap: 16px;
}

.error-text {
  color: #ff3b30;
  font-size: 16px;
}

.retry-btn {
  padding: 8px 16px;
  background-color: #0071e3;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
}

.retry-btn:hover {
  background-color: #0077ed;
}


/* 模态框 */
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
  animation: fadeIn 0.2s ease;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.modal-content {
  background-color: #ffffff;
  border-radius: 16px;
  max-width: 600px;
  width: 90%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  animation: slideUp 0.3s ease;
  position: relative;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.close-btn {
  position: absolute;
  top: 16px;
  right: 16px;
  width: 32px;
  height: 32px;
  border: none;
  background-color: #f5f5f7;
  border-radius: 50%;
  font-size: 18px;
  cursor: pointer;
  transition: all 0.2s ease;
  z-index: 10;
}

.close-btn:hover {
  background-color: #e8e8ed;
}

.modal-header {
  padding: 24px 60px 16px 24px;
  border-bottom: 1px solid #f5f5f7;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 12px;
}

.modal-header h2 {
  font-size: 24px;
  font-weight: 700;
  color: #1d1d1f;
  flex: 1;
}

.modal-body {
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.detail-section {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.detail-section h4 {
  font-size: 15px;
  font-weight: 600;
  color: #1d1d1f;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: #86868b;
}

.detail-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.detail-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.detail-label {
  font-size: 12px;
  color: #86868b;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-weight: 600;
}

.detail-value {
  font-size: 15px;
  color: #1d1d1f;
  font-weight: 500;
}

.detail-section p {
  font-size: 15px;
  color: #1d1d1f;
  line-height: 1.6;
}

.suggestions-list {
  list-style: none;
  padding-left: 0;
}

.suggestions-list li {
  font-size: 15px;
  color: #1d1d1f;
  padding: 8px 0;
  padding-left: 20px;
  position: relative;
  line-height: 1.6;
}

.suggestions-list li:before {
  content: '•';
  position: absolute;
  left: 0;
  color: #0071e3;
  font-weight: bold;
}

.links-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.link-item {
  font-size: 15px;
  color: #0071e3;
  text-decoration: none;
  padding: 10px 12px;
  background-color: #f5f5f7;
  border-radius: 8px;
  transition: all 0.2s ease;
  display: inline-block;
  width: fit-content;
}

.link-item:hover {
  background-color: #e8e8ed;
  text-decoration: underline;
}

@media (max-width: 768px) {
  .detail-grid {
    grid-template-columns: 1fr;
  }

  .competitions-grid {
    grid-template-columns: 1fr;
  }

  .filter-bar {
    flex-direction: column;
    align-items: stretch;
  }

  .search-box {
    min-width: unset;
  }

  .filters {
    flex-direction: column;
    width: 100%;
  }

  .filter-group {
    width: 100%;
  }

  .filter-select {
    width: 100%;
  }
}
</style>
