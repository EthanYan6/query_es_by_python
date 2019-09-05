# query_es_by_python
Use python to encapsulate a set of APIs for query es

# API 设计文档

## 查询所有数据

```http
API:    GET /siemens/matchall/(?P<index>[a-z_]+)/
参数:
index    // 索引名称
响应:
由每个文档（json数据）组成的列表（查询结果中_source）
```

> 可以查询小数据量的索引（10000条以内），也可以查询大数据量的索引（10000条以上）。
>
> **问题**：返回结果有延时，体验度不好
