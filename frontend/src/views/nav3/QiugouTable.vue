<template>
  <section>
    <!--工具条-->
    <el-col :span="24" class="toolbar" style="padding-bottom: 0px">
      <el-form :inline="true" :model="filters">
        <el-form-item>
          <el-input v-model="filters.filter" placeholder="关键字"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" v-on:click="getPosts">查询</el-button>
        </el-form-item>
      </el-form>
    </el-col>

    <!--列表-->
    <el-table
      :data="qiugous"
      highlight-current-row
      v-loading="listLoading"
      @selection-change="selsChange"
      style="width: 100%"
    >
      <el-table-column prop="userid" label="用户id" width="120" sortable>
      </el-table-column>
      <el-table-column prop="title" label="标题" width="140" sortable>
      </el-table-column>
      <el-table-column prop="intro" label="详情" width="180" sortable>
      </el-table-column>
      <el-table-column prop="tag" label="标签" width="120" sortable>
      </el-table-column>
      <el-table-column prop="price" label="价格" width="140" sortable>
      </el-table-column>
      <el-table-column prop="campus" label="校区" width="120" sortable>
      </el-table-column>
      <el-table-column prop="condition" label="新旧" width="120" sortable>
      </el-table-column>
      <el-table-column prop="time" label="日期" width="180" sortable>
      </el-table-column>
      <el-table-column label="操作" width="100">
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
import { getQiugouList, removeQiugou, getQiugouFilter } from "../../api/api";
//import NProgress from 'nprogress'
import {
  getGoodList,
  removeGood,
  batchRemoveUser,
  editUser,
} from "../../api/api";

export default {
  data() {
    return {
      filters: {
        name: "",
      },
      qiugous: [],
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
      this.getPosts();
    },
    //获取用户列表
    getPosts() {
      let para = {
        page: this.page,
        filter: this.filters.filter,
      };
      this.listLoading = true;
      //NProgress.start();
      getQiugouFilter(para).then((res) => {
        this.total = res.data;
        this.qiugous = res.data;
        this.listLoading = false;
        //NProgress.done();
      });
    },
    //删除
    handleDel: function (index, row) {
      this.$confirm("确认删除该求购吗?", "提示", {
        type: "warning",
      })
        .then(() => {
          this.listLoading = true;
          //NProgress.start();
          let para = { id: row.postid };
          removeQiugou(para).then((res) => {
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
    this.getPosts();
  },
};
</script>

<style scoped></style>
