{{/*
Expand the name of the chart.
*/}}
{{- define "pt-backend.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}


{{/*
Expand the nameid of the chart.
*/}}
{{- define "pt-backend.nameid" -}}
{{- printf "%s-%s" (include "pt-backend.name" .) .Chart.Version }}
{{- end }}

{{/*
Get main config file.
*/}}
{{- define "pt-backend.main" -}}
{{- $encryptedFile := .Files.Get "files/secrets.yaml.enc" }}
{{- $salt := $encryptedFile | substr 0 64 }}
{{- $remainingFile := $encryptedFile | substr 64 -1 }}
{{- $ivAndEncryptedData := $remainingFile | b64enc }}
{{- $passphraseWithSalt :=  (printf "%s%s" .Values.aesPassphrase $salt) | sha256sum | substr 0 32 }}
{{- $secrets := $ivAndEncryptedData | decryptAES $passphraseWithSalt | fromYaml -}}
{{- $_ := set $secrets "Template" $.Template }}
{{- tpl (.Files.Get "files/main.yml") $secrets -}}
{{- end -}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "pt-backend.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "pt-backend.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "pt-backend.labels" -}}
helm.sh/chart: {{ include "pt-backend.chart" . }}
{{ include "pt-backend.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "pt-backend.selectorLabels" -}}
app.kubernetes.io/name: {{ include "pt-backend.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "pt-backend.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "pt-backend.fullname" .) .Values.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.serviceAccount.name }}
{{- end }}
{{- end }}
