<template>
  <div class="guide">
    <div class="guide-container">
      <h2>竞赛指导</h2>

      <div class="guide-content">
        <section class="guide-section">
          <h3>选择合适的竞赛</h3>
          <p>
            选择竞赛时应综合考虑自身兴趣、专业方向和技能水平。建议：
          </p>
          <ul>
            <li>明确自己的学习方向和职业规划</li>
            <li>选择与专业相关或感兴趣的领域</li>
            <li>根据能力选择难度合适的竞赛</li>
            <li>参考往年获奖作品找到差距</li>
          </ul>
        </section>

        <section class="guide-section">
          <h3>竞赛准备指南</h3>
          <p>充分的准备是成功的基础，这里是一些建议：</p>
          <ul>
            <li><strong>了解赛事规则</strong>：仔细阅读竞赛官方文件，理解评分标准</li>
            <li><strong>组建合适的团队</strong>：选择技能互补的队员，确保良好的沟通</li>
            <li><strong>制定详细计划</strong>：从立项到提交要合理分配时间</li>
            <li><strong>技术积累</strong>：参赛前系统学习相关领域的技术知识</li>
            <li><strong>作品打磨</strong>：不断优化代码质量和用户体验</li>
            <li><strong>文档准备</strong>：编写清晰的技术文档和使用说明</li>
          </ul>
        </section>

        <section class="guide-section">
          <h3>常见竞赛类型</h3>
          <div class="competition-types">
            <div class="type-card">
              <h4>算法竞赛</h4>
              <p>如：蓝桥杯、ACM-ICPC</p>
              <p class="tips">重点：算法设计、数据结构、代码优化</p>
            </div>
            <div class="type-card">
              <h4>创意创新竞赛</h4>
              <p>如：互联网+、全国计算机设计大赛</p>
              <p class="tips">重点：创新性、应用价值、完整性</p>
            </div>
            <div class="type-card">
              <h4>数学建模竞赛</h4>
              <p>如：全国大学生数学建模大赛</p>
              <p class="tips">重点：建模思路、数学理论、求解方法</p>
            </div>
            <div class="type-card">
              <h4>编程应用竞赛</h4>
              <p>如：iCan创新创业</p>
              <p class="tips">重点：实用性、创新、用户体验</p>
            </div>
          </div>
        </section>

        <section class="guide-section">
          <h3>参赛建议</h3>
          <div class="tips-box">
            <div class="tip-item">
              <span class="tip-icon">✓</span>
              <div>
                <strong>做</strong>：尽早开始、持续学习、团队协作、充分准备、追求品质
              </div>
            </div>
            <div class="tip-item">
              <span class="tip-icon error">✗</span>
              <div>
                <strong>避免</strong>：临时抱佛脚、单打独斗、忽视细节、过度创新、盲目跟风
              </div>
            </div>
          </div>
        </section>

        <section class="guide-section">
          <h3>常见问题</h3>
          <div class="faq">
            <div class="faq-item">
              <h5>Q：作为新手，应该参加什么级别的竞赛？</h5>
              <p>A：建议从校级竞赛开始，积累经验后逐步参加省级和国家级竞赛。这样可以避免打击自信心，同时稳步提升能力。</p>
            </div>
            <div class="faq-item">
              <h5>Q：竞赛和学业冲突怎么办？</h5>
              <p>A：合理规划时间，不要让竞赛影响主要学业。通常建议在寒暑假或学期末集中参加竞赛。</p>
            </div>
            <div class="faq-item">
              <h5>Q：参加多个竞赛会不会太累？</h5>
              <p>A：建议不超过3-4个竞赛同时进行。重点做好1-2个主要竞赛，其他竞赛可作为补充。</p>
            </div>
            <div class="faq-item">
              <h5>Q：没有获奖还有意义吗？</h5>
              <p>A：参赛过程本身就是学习和成长。即使没有获奖，也能学到知识、锻炼能力、积累经验，这些对未来都是有益的。</p>
            </div>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Guide'
}
</script>

<style scoped>
.guide {
  height: 100%;
  overflow-y: auto;
  background-color: #ffffff;
}

.guide-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 40px 24px;
}

.guide-container h2 {
  font-size: 32px;
  font-weight: 700;
  color: #1d1d1f;
  margin-bottom: 32px;
}

.guide-content {
  display: flex;
  flex-direction: column;
  gap: 40px;
}

.guide-section {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.guide-section h3 {
  font-size: 20px;
  font-weight: 600;
  color: #1d1d1f;
  margin-bottom: 8px;
}

.guide-section p {
  font-size: 15px;
  color: #1d1d1f;
  line-height: 1.6;
  margin-bottom: 8px;
}

.guide-section ul {
  padding-left: 24px;
  list-style: none;
}

.guide-section li {
  font-size: 15px;
  color: #1d1d1f;
  line-height: 1.8;
  margin-bottom: 8px;
  position: relative;
  padding-left: 8px;
}

.guide-section li:before {
  content: '•';
  position: absolute;
  left: -16px;
  color: #0071e3;
  font-weight: bold;
}

/* 竞赛类型卡片 */
.competition-types {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
  margin-top: 12px;
}

.type-card {
  padding: 16px;
  background-color: #f5f5f7;
  border-radius: 12px;
  border: 1px solid #e8e8ed;
}

.type-card h4 {
  font-size: 15px;
  font-weight: 600;
  color: #1d1d1f;
  margin-bottom: 8px;
}

.type-card p {
  font-size: 14px;
  color: #86868b;
  margin: 0;
  line-height: 1.5;
}

.type-card .tips {
  margin-top: 8px;
  padding-top: 8px;
  border-top: 1px solid #d2d2d7;
  color: #0071e3 !important;
  font-weight: 500;
}

/* 建议框 */
.tips-box {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-top: 12px;
}

.tip-item {
  display: flex;
  gap: 12px;
  padding: 14px 16px;
  background-color: #f5f5f7;
  border-radius: 8px;
  border-left: 4px solid #0071e3;
}

.tip-item.error {
  border-left-color: #ff3b30;
}

.tip-icon {
  font-size: 16px;
  font-weight: bold;
  color: #0071e3;
  flex-shrink: 0;
  width: 24px;
  text-align: center;
}

.tip-item.error .tip-icon {
  color: #ff3b30;
}

.tip-item div {
  font-size: 15px;
  color: #1d1d1f;
  line-height: 1.5;
}

.tip-item strong {
  color: #1d1d1f;
}

/* 常见问题 */
.faq {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-top: 12px;
}

.faq-item {
  padding: 16px;
  background-color: #f5f5f7;
  border-radius: 8px;
}

.faq-item h5 {
  font-size: 15px;
  font-weight: 600;
  color: #1d1d1f;
  margin: 0 0 8px 0;
}

.faq-item p {
  font-size: 14px;
  color: #86868b;
  margin: 0;
  line-height: 1.6;
}

@media (max-width: 768px) {
  .competition-types {
    grid-template-columns: 1fr;
  }

  .guide-container {
    padding: 24px 16px;
  }

  .guide-container h2 {
    font-size: 24px;
    margin-bottom: 24px;
  }

  .guide-content {
    gap: 24px;
  }
}
</style>
