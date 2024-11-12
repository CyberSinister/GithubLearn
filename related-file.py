dsfsdafsdfasff
def a = ('b', 'g', 'a', 'd', 'f', 'c', 'h', 'e')
x = sorted(a)
print(x)<template>
<div class='filter-box'>
<div class='left-box'>
<el-input placeholder='请输入授权名称' v-model='filter.name' class='common-input' @input='query' clearable suffix-icon='el-icon-search' />
</div>
<div class='right-box'>
 <el-button type='primary'>新建授权申请</el-button>
</div>
 </div>
</template>
    
<script lang='ts'>
import { defineComponent, reactive } from 'vue'
    
export default defineComponent({
name: 'filter-box',
emits: ['query'],
setup(props, _) {
const filter = reactive({
  name: ''
})
  const query = () => {
 _.emit('query', filter)
}
  return {
  filter,
  query
 }
}
})
</script>
    
<style lang='stylus' scoped>
.filter-box
  display flex
  height 32px
  justify-content space-between
  margin-bottom 16px
</style>
    fs
    fa
    x = {'apple', 'banana', 'cherry'}
    y = {'google', 'microsoft', 'apple'}
    z = x.difference(y)
    print(z)asdf(self):
    """
    Purpose: 
    """
    
# end def