# 高级特性

> 加载条件：显式需要时触发，各节独立

## Behavior-Code 逐行对照
> 实现完接口需要对照验证时触发

每个接口实现模块的代码应与蓝图 BEHAVIOR 声明逐行对照：

| 声明项 | 蓝图中写什么 | 代码中有什么 |
|--------|-------------|------------|
| pre | if not filepath: raise ValueError | 相同的预条件检查 |
| post | 返回含 id 的 Category 对象 | return {"id": ...} |
| error | ValueError, TypeError, IOError | 对应的异常 |
| side-effect | _data 追加一条记录 | data["x"].append(item) |

对照方式：
1. 对每个接口，从代码中找 pre 检查 → 确认存在 ✓
2. 找 return → 符合 post ✓
3. 找 raise → 覆盖所有 error ✓
4. 找 data 修改 → 匹配 side-effect ✓

## Auto-Checkpoint
> 模块标记 [done] 后触发

每个 [done] 后写入 CHECKPOINT.md：
```
@CHECKPOINT
  时间: Phase 2 / categories 完成
  状态: 2/6 模块 done
  进度: storage [done], categories [done]
  最后变更: @CHANGE_001
  下一步: transactions
```

格式：CHECKPOINT 为纯 Markdown，无 @ 前缀冲突。

## Design Decision Log
> 选择设计方案时触发

需要记录设计决策时，在 BLUEPRINT.md 中加入 @DECISION：

```
@DECISION
  标题: 选择 JSON 而非 SQLite 作为存储方案
  理由: 本项目为单机 CLI 工具，数据量小，JSON 无需额外依赖
  放弃的方案: SQLite（需要 sqlite3 库）
  影响: 无复杂查询能力，但本项目不需要
```

规则：
- 每条 @DECISION 有标题和理由
- 重要决策记录被放弃的方案
- 不要为每个选择都记录，只记"非显而易见"非显而易见"的

## 并行填充策略
> 同层 ≥ 2 模块 [empty] 时触发

同层无依赖关系的模块可以并行填充：

```
条件：模块 A 和 B 同层且无相互依赖
方法：Task（子任务）并行实现
输出：两个模块的代码 + 各自的 Behavior 对照
风险：接口命名风格不一致 → 填充完成后统一检查
```

不满足条件时串行。

## 多会话协作协议
> 多人协作场景触发

多会话协作流程：

```
全局 LOCKS.md 维护锁状态：
  @LOCK storage     session_1
  @LOCK categories  session_2
  @LOCK transactions free

同时只能有一个会话拿到模块锁。
跨会话依赖：访问 [done] 模块时只读不写。
合并流程：所有会话完成后，由全局任务合并 BLUEPRINT.md。
```

## 退出条件
> 用户问"什么时候退出 skill"时触发

```
完成条件（满足任一即可退出）：
1. Phase 3 验证通过，全部 [done]
2. 用户说"停"、"不用继续了"、"够了"
3. Phase 1 用户不满意蓝图，放弃项目
4. 连续 3 次约束违规被暂停

退出后保留 .arch/ 目录，可随时恢复。
```

## @CHANGE vs @DECISION 边界
> 修改蓝图需要区分变更类型时触发

```
@CHANGE：记录了"做了什么修改"，面向开发过程
@DECISION：记录了"为什么这么设计"，面向架构理解

变更蓝图的场景 → @CHANGE
选择设计方案的场景 → @DECISION

边界模糊时的判断方法：
- 这个条目是否影响其他模块的接口签名？→ @CHANGE
- 这个条目是否记录了被放弃的替代方案？→ @DECISION
```

## Rollback 协议
> 下游模块因上游变更无法对接时触发

```
触发条件：Phase 2 填充时发现依赖模块的接口签名变了
          导致下游模块对接不上

步骤：
1. 暂停下游模块
2. 检查 @CHANGE 最近的变更
3. 如果上游接口变化是合理的 → 更新下游接口调用
4. 如果上游接口变化是不合理的 → 回滚上游的变更
5. 记录 @CHANGE 描述回滚
```

## 测试策略
> 模块 [done] 后生成测试时触发

从 BEHAVIOR 声明自动生成测试：

```python
# 对应蓝图 addCategory 的 pre/post/error
def test_addCategory_pre_name_empty():
    with pytest.raises(ValueError):
        addCategory("", "income")

def test_addCategory_post_id_positive():
    cat = addCategory("test", "income")
    assert cat["id"] > 0
```

每个 pre/error → 一个异常测试
每个 post → 一个断言测试
每个 side-effect → 数据状态验证

## 验收清单
> Phase 3 完成后触发

```
□ 每个 @MODULE 状态为 [done]
□ 每条 @FLOW 至少执行一次并产生输出
□ 错误链 EC1/EC2/EC3 全部检查
□ @CHANGE 无待处理条目
□ SUMMARY.md 已生成
□ 用户确认"看起来没问题"
```