Dim App 'As Application
Set App = CreateObject("QuickTest.Application")
App.Launch
App.Visible = True
App.Test.Settings.Launchers("Windows Applications").Active = True
App.Test.Settings.Launchers("Windows Applications").Applications.RemoveAll
App.Test.Settings.Launchers("Windows Applications").Applications.AddApplication "C:\Users\dell\Desktop\0_C4226_SWTesting\Project\code\dist\secure\secure.exe", "", "", TRUE, TRUE
App.Test.Settings.Launchers("Windows Applications").RecordOnQTDescendants = False
App.Test.Settings.Launchers("Windows Applications").RecordOnExplorerDescendants = False
App.Test.Settings.Launchers("Windows Applications").RecordOnSpecifiedApplications = True
App.Test.Settings.Run.IterationMode = "rngAll"
App.Test.Settings.Run.StartIteration = 1
App.Test.Settings.Run.EndIteration = 1
App.Test.Settings.Run.ObjectSyncTimeOut = 20000
App.Test.Settings.Run.DisableSmartIdentification = False
App.Test.Settings.Run.OnError = "Dialog"
App.Test.Settings.Resources.DataTablePath = "<Default>"
App.Test.Settings.Resources.Libraries.RemoveAll
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' System Local Monitoring settings
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
App.Test.Settings.LocalSystemMonitor.Enable = false
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Log Tracking settings
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
With App.Test.Settings.LogTracking
	.IncludeInResults = False
	.Port = 18081
	.IP = "127.0.0.1"
	.MinTriggerLevel = "ERROR"
	.EnableAutoConfig = False
	.RecoverConfigAfterRun = False
	.ConfigFile = ""
	.MinConfigLevel = "WARN"
End With
