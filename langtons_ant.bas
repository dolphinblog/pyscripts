Private Declare PtrSafe Sub Sleep Lib "kernel32" (ByVal dwMilliseconds As Long)
Sub lant()
    
    'Author: Vinson <vinson_wei@126.com>
    Dim cnt&, maxCnt&, flag%
    Dim markColor$
    Dim antAtColor$
    Dim antDirection%
    Dim sleepTime%
    Dim ant As Range, oldAnt As Range

    '定义表示蚂蚁方向的符号
    Dim d
    Set d = CreateObject("scripting.dictionary")
    d.Add 0, "↑"
    d.Add 1, "→"
    d.Add 2, "↓"
    d.Add 3, "←"
    
    '初始参数设置
    Set ant = Cells(100, 100)
    markColor = 15773696
    antDirection = 0
    cnt = 0
    flag = 0
    maxCnt = 20000
    sleepTime = 200

    '清理上次运行痕迹
    ActiveSheet.Columns.clear
    
    '显示蚂蚁初始位置
    directionNumber = (antDirection / 90) Mod 4
    directionSymbol = d(directionNumber)
    ant.Value = directionSymbol
    
    Do '开始循环

    cnt = cnt + 1
    Application.StatusBar = "第" & cnt & "步"
    DoEvents

    '1. 获取下一个单元格方向
    If ant.Interior.Color <> markColor Then
        '非黑格
        antDirection = antDirection + 90
        flag = 1
    Else
        '黑格
        antDirection = antDirection - 90
        flag = 0
    End If

    antDirection = antDirection Mod 360
    
    '2. 获取下一个单元格地址
    directionNumber = ((antDirection + 360) / 90) Mod 4
    directionSymbol = d(directionNumber)
    Set oldAnt = ant
    
    Select Case directionNumber
        Case 0:
            Set ant = ant.Offset(-1, 0)
        Case 1:
            Set ant = ant.Offset(0, 1)
        Case 2:
            Set ant = ant.Offset(1, 0)
        Case 3:
            Set ant = ant.Offset(0, -1)
    End Select

    '3. 下一个单元格符号后出现,当前单元格符号消失,同时修改当前单元格颜色(如果需要)
    Sleep sleepTime
    oldAnt.Value = directionSymbol
    Sleep sleepTime
    ant.Value = directionSymbol
    Sleep sleepTime
    oldAnt.Value = ""
    If flag Then
        oldAnt.Interior.Color = markColor
    Else
        oldAnt.Interior.Pattern = xlNone
    End If
                                        
    Loop While cnt < maxCnt

End Sub
