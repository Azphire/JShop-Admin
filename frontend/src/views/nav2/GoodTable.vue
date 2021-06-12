<template>
  <section>
    <!--工具条-->
    <el-col :span="24" class="toolbar" style="padding-bottom: 0px">
      <el-form :inline="true" :model="filters">
        <el-form-item>
          <el-input v-model="filters.filter" placeholder="关键字"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" v-on:click="getGoods">查询</el-button>
        </el-form-item>
      </el-form>
    </el-col>

    <!--列表-->
    <el-table
      :data="goods"
      highlight-current-row
      v-loading="listLoading"
      @selection-change="selsChange"
      style="width: 100%"
    >
      <el-table-column type="selection" width="55"> </el-table-column>
      <el-table-column prop="sellerid" label="用户id" width="100" sortable>
      </el-table-column>
      <el-table-column prop="name" label="商品名" width="150" sortable>
      </el-table-column>
      <el-table-column prop="price" label="价格" width="100" sortable>
      </el-table-column>
      <el-table-column prop="description" label="描述" width="250" sortable>
      </el-table-column>
      <el-table-column prop="campus" label="校区" width="90" sortable>
      </el-table-column>
      <el-table-column prop="old" label="新旧" width="90" sortable>
      </el-table-column>
      <el-table-column prop="publishdate" label="日期" width="170" sortable>
      </el-table-column>
      <el-table-column prop="tag" label="标签" width="90" sortable>
      </el-table-column>
      <el-table-column label="操作" width="150">
        <template scope="scope">
          <el-button
            type="danger"
            size="small"
            @click="handleDel(scope.$index, scope.row)"
            >删除</el-button
          >
        </template>
      </el-table-column>
    </el-table>

    <!--工具条-->
    <el-col :span="24" class="toolbar">
      <el-button
        type="danger"
        @click="batchRemove"
        :disabled="this.sels.length === 0"
        >批量删除</el-button
      >
      <el-pagination
        layout="prev, pager, next"
        @current-change="handleCurrentChange"
        :page-size="20"
        :total="total"
        style="float: right"
      >
      </el-pagination>
    </el-col>
  </section>
</template>

<script>
import util from "../../common/js/util";
//import NProgress from 'nprogress'
import {
  getGoodList,
  removeGood,
  batchRemoveUser,
  editUser,
  getGoodFilter,
} from "../../api/api";

export default {
  data() {
    return {
      filters: {
        name: "",
      },
      goods: [],
      total: 0,
      page: 1,
      listLoading: false,
      sels: [], //列表选中列

      editFormVisible: false, //编辑界面是否显示
      editLoading: false,
      editFormRules: {
        name: [{ required: true, message: "请输入姓名", trigger: "blur" }],
      },
      //编辑界面数据
      editForm: {
        name: "",
        nick: "",
        campus: 0,
      },

      addLoading: false,
      addFormRules: {
        name: [{ required: true, message: "请输入姓名", trigger: "blur" }],
      },
    };
  },
  methods: {
    handleCurrentChange(val) {
      this.page = val;
      this.getGoods();
    },
    //获取用户列表
    getGoods() {
      let para = {
        page: this.page,
        filter: this.filters.filter,
      };
      this.listLoading = true;
      //NProgress.start();
      getGoodFilter(para).then((res) => {
        this.total = res.data;
        this.goods = res.data;
        this.listLoading = false;
        //NProgress.done();
      });
    },
    //删除
    handleDel: function (index, row) {
      this.$confirm("确认删除该商品吗?", "提示", {
        type: "warning",
      })
        .then(() => {
          this.listLoading = true;
          //NProgress.start();
          let para = { id: row.goodid };
          removeGood(para).then((res) => {
            this.listLoading = false;
            //NProgress.done();
            this.$message({
              message: "删除成功",
              type: "success",
            });
            this.getGoods();
          });
        })
        .catch(() => {});
    },
    //显示编辑界面
    handleEdit: function (index, row) {
      this.editFormVisible = true;
      this.editForm = Object.assign({}, row);
    },
    selsChange: function (sels) {
      this.sels = sels;
    },
    //批量删除
    batchRemove: function () {
      var ids = this.sels.map((item) => item.id).toString();
      this.$confirm("确认删除选中记录吗？", "提示", {
        type: "warning",
      })
        .then(() => {
          this.listLoading = true;
          //NProgress.start();
          let para = { ids: ids };
          batchRemoveUser(para).then((res) => {
            this.listLoading = false;
            //NProgress.done();
            this.$message({
              message: "删除成功",
              type: "success",
            });
            this.getGoods();
          });
        })
        .catch(() => {});
    },
  },
  mounted() {
    this.getGoods();
  },
};
</script>

<style scoped></style>
