--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.3
-- Dumped by pg_dump version 9.5.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: scapp; Type: SCHEMA; Schema: -; Owner: scapp
--

CREATE SCHEMA scapp;


ALTER SCHEMA scapp OWNER TO scapp;

SET search_path = scapp, pg_catalog;

--
-- Name: on_update_current_timestamp_modified_at(); Type: FUNCTION; Schema: scapp; Owner: scapp
--

CREATE FUNCTION on_update_current_timestamp_modified_at() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
   NEW.modified_at = now();
   RETURN NEW;
END;
$$;


ALTER FUNCTION scapp.on_update_current_timestamp_modified_at() OWNER TO scapp;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: category_projects_all; Type: TABLE; Schema: scapp; Owner: scapp
--

CREATE TABLE category_projects_all (
    cpa_id bigint NOT NULL,
    cca_id bigint NOT NULL,
    cpoa_id bigint,
    tua_id bigint,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    created_by character varying(30) NOT NULL,
    modified_at timestamp with time zone DEFAULT now() NOT NULL,
    modified_by character varying(30) NOT NULL,
    cpa_code character varying(30) NOT NULL,
    cpa_title character varying(160) NOT NULL,
    cpa_title_deleted character varying(160),
    cpa_summary character varying(512),
    cpa_url character varying(160) NOT NULL,
    cpa_url_deleted character varying(160),
    cpa_deleted boolean NOT NULL,
    cpa_deleted_date timestamp with time zone,
    cpa_deleted_by character varying(30)
);


ALTER TABLE category_projects_all OWNER TO scapp;

--
-- Name: category_projects_all_cpa_id_seq; Type: SEQUENCE; Schema: scapp; Owner: scapp
--

CREATE SEQUENCE category_projects_all_cpa_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE category_projects_all_cpa_id_seq OWNER TO scapp;

--
-- Name: category_projects_all_cpa_id_seq; Type: SEQUENCE OWNED BY; Schema: scapp; Owner: scapp
--

ALTER SEQUENCE category_projects_all_cpa_id_seq OWNED BY category_projects_all.cpa_id;


--
-- Name: client_categories_all; Type: TABLE; Schema: scapp; Owner: scapp
--

CREATE TABLE client_categories_all (
    cca_id bigint NOT NULL,
    pca_id bigint NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    created_by character varying(30) NOT NULL,
    modified_at timestamp with time zone DEFAULT now() NOT NULL,
    modified_by character varying(30) NOT NULL,
    cca_code character varying(30) NOT NULL,
    cca_name character varying(128) NOT NULL
);


ALTER TABLE client_categories_all OWNER TO scapp;

--
-- Name: client_categories_all_cca_id_seq; Type: SEQUENCE; Schema: scapp; Owner: scapp
--

CREATE SEQUENCE client_categories_all_cca_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE client_categories_all_cca_id_seq OWNER TO scapp;

--
-- Name: client_categories_all_cca_id_seq; Type: SEQUENCE OWNED BY; Schema: scapp; Owner: scapp
--

ALTER SEQUENCE client_categories_all_cca_id_seq OWNED BY client_categories_all.cca_id;


--
-- Name: client_purchase_orders_all; Type: TABLE; Schema: scapp; Owner: scapp
--

CREATE TABLE client_purchase_orders_all (
    cpoa_id bigint NOT NULL,
    pca_id bigint NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    created_by character varying(30) NOT NULL,
    modified_at timestamp with time zone DEFAULT now() NOT NULL,
    modified_by character varying(30) NOT NULL,
    cpoa_number character varying(30) NOT NULL,
    cpoa_date timestamp with time zone NOT NULL,
    cpoa_total numeric(17,2) NOT NULL,
    cpoa_soa text
);


ALTER TABLE client_purchase_orders_all OWNER TO scapp;

--
-- Name: client_purchase_orders_all_cpoa_id_seq; Type: SEQUENCE; Schema: scapp; Owner: scapp
--

CREATE SEQUENCE client_purchase_orders_all_cpoa_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE client_purchase_orders_all_cpoa_id_seq OWNER TO scapp;

--
-- Name: client_purchase_orders_all_cpoa_id_seq; Type: SEQUENCE OWNED BY; Schema: scapp; Owner: scapp
--

ALTER SEQUENCE client_purchase_orders_all_cpoa_id_seq OWNED BY client_purchase_orders_all.cpoa_id;


--
-- Name: client_teams_all; Type: TABLE; Schema: scapp; Owner: scapp
--

CREATE TABLE client_teams_all (
    cta_id bigint NOT NULL,
    pca_id bigint NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    created_by character varying(30) NOT NULL,
    modified_at timestamp with time zone DEFAULT now() NOT NULL,
    modified_by character varying(30) NOT NULL,
    cta_code character varying(30) NOT NULL,
    cta_name character varying(128) NOT NULL
);


ALTER TABLE client_teams_all OWNER TO scapp;

--
-- Name: client_teams_all_cta_id_seq; Type: SEQUENCE; Schema: scapp; Owner: scapp
--

CREATE SEQUENCE client_teams_all_cta_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE client_teams_all_cta_id_seq OWNER TO scapp;

--
-- Name: client_teams_all_cta_id_seq; Type: SEQUENCE OWNED BY; Schema: scapp; Owner: scapp
--

ALTER SEQUENCE client_teams_all_cta_id_seq OWNED BY client_teams_all.cta_id;


--
-- Name: client_users_all; Type: TABLE; Schema: scapp; Owner: scapp
--

CREATE TABLE client_users_all (
    cua_id bigint NOT NULL,
    pca_id bigint NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    created_by character varying(30) NOT NULL,
    modified_at timestamp with time zone DEFAULT now() NOT NULL,
    modified_by character varying(30) NOT NULL,
    cua_username character varying(30) NOT NULL,
    cua_email character varying(128) NOT NULL,
    cua_fname character varying(45) NOT NULL,
    cua_lname character varying(45) NOT NULL,
    cua_mname character varying(45)
);


ALTER TABLE client_users_all OWNER TO scapp;

--
-- Name: client_users_all_cua_id_seq; Type: SEQUENCE; Schema: scapp; Owner: scapp
--

CREATE SEQUENCE client_users_all_cua_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE client_users_all_cua_id_seq OWNER TO scapp;

--
-- Name: client_users_all_cua_id_seq; Type: SEQUENCE OWNED BY; Schema: scapp; Owner: scapp
--

ALTER SEQUENCE client_users_all_cua_id_seq OWNED BY client_users_all.cua_id;


--
-- Name: portal_clients_all; Type: TABLE; Schema: scapp; Owner: scapp
--

CREATE TABLE portal_clients_all (
    pca_id bigint NOT NULL,
    pa_id bigint NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    created_by character varying(30) NOT NULL,
    modified_at timestamp with time zone DEFAULT now() NOT NULL,
    modified_by character varying(30) NOT NULL,
    pca_code character varying(30) NOT NULL,
    pca_name character varying(128) NOT NULL
);


ALTER TABLE portal_clients_all OWNER TO scapp;

--
-- Name: portal_clients_all_pca_id_seq; Type: SEQUENCE; Schema: scapp; Owner: scapp
--

CREATE SEQUENCE portal_clients_all_pca_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE portal_clients_all_pca_id_seq OWNER TO scapp;

--
-- Name: portal_clients_all_pca_id_seq; Type: SEQUENCE OWNED BY; Schema: scapp; Owner: scapp
--

ALTER SEQUENCE portal_clients_all_pca_id_seq OWNED BY portal_clients_all.pca_id;


--
-- Name: portals_all; Type: TABLE; Schema: scapp; Owner: scapp
--

CREATE TABLE portals_all (
    pa_id bigint NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    created_by character varying(30) NOT NULL,
    modified_at timestamp with time zone DEFAULT now() NOT NULL,
    modified_by character varying(30) NOT NULL,
    pa_code character varying(30) NOT NULL,
    pa_name character varying(128) NOT NULL,
    pa_desc character varying(512) NOT NULL
);


ALTER TABLE portals_all OWNER TO scapp;

--
-- Name: portals_all_pa_id_seq; Type: SEQUENCE; Schema: scapp; Owner: scapp
--

CREATE SEQUENCE portals_all_pa_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE portals_all_pa_id_seq OWNER TO scapp;

--
-- Name: portals_all_pa_id_seq; Type: SEQUENCE OWNED BY; Schema: scapp; Owner: scapp
--

ALTER SEQUENCE portals_all_pa_id_seq OWNED BY portals_all.pa_id;


--
-- Name: project_worklogs_all; Type: TABLE; Schema: scapp; Owner: scapp
--

CREATE TABLE project_worklogs_all (
    pwa_id bigint NOT NULL,
    cpa_id bigint NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    created_by character varying(30) NOT NULL,
    modified_at timestamp with time zone DEFAULT now() NOT NULL,
    modified_by character varying(30) NOT NULL,
    pwa_note text NOT NULL
);


ALTER TABLE project_worklogs_all OWNER TO scapp;

--
-- Name: project_worklogs_all_pwa_id_seq; Type: SEQUENCE; Schema: scapp; Owner: scapp
--

CREATE SEQUENCE project_worklogs_all_pwa_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE project_worklogs_all_pwa_id_seq OWNER TO scapp;

--
-- Name: project_worklogs_all_pwa_id_seq; Type: SEQUENCE OWNED BY; Schema: scapp; Owner: scapp
--

ALTER SEQUENCE project_worklogs_all_pwa_id_seq OWNED BY project_worklogs_all.pwa_id;


--
-- Name: team_users_all; Type: TABLE; Schema: scapp; Owner: scapp
--

CREATE TABLE team_users_all (
    tua_id bigint NOT NULL,
    cta_id bigint NOT NULL,
    cua_id bigint NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    created_by character varying(30) NOT NULL,
    modified_at timestamp with time zone DEFAULT now() NOT NULL,
    modified_by character varying(30) NOT NULL,
    tua_active boolean NOT NULL,
    tua_role character varying(45) NOT NULL
);


ALTER TABLE team_users_all OWNER TO scapp;

--
-- Name: team_users_all_tua_id_seq; Type: SEQUENCE; Schema: scapp; Owner: scapp
--

CREATE SEQUENCE team_users_all_tua_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE team_users_all_tua_id_seq OWNER TO scapp;

--
-- Name: team_users_all_tua_id_seq; Type: SEQUENCE OWNED BY; Schema: scapp; Owner: scapp
--

ALTER SEQUENCE team_users_all_tua_id_seq OWNED BY team_users_all.tua_id;


--
-- Name: worklog_actions_all; Type: TABLE; Schema: scapp; Owner: scapp
--

CREATE TABLE worklog_actions_all (
    waa_id bigint NOT NULL,
    pwa_id bigint NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    created_by character varying(30) NOT NULL,
    modified_at timestamp with time zone DEFAULT now() NOT NULL,
    modified_by character varying(30) NOT NULL,
    waa_type smallint NOT NULL,
    waa_value text NOT NULL
);


ALTER TABLE worklog_actions_all OWNER TO scapp;

--
-- Name: worklog_actions_all_waa_id_seq; Type: SEQUENCE; Schema: scapp; Owner: scapp
--

CREATE SEQUENCE worklog_actions_all_waa_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE worklog_actions_all_waa_id_seq OWNER TO scapp;

--
-- Name: worklog_actions_all_waa_id_seq; Type: SEQUENCE OWNED BY; Schema: scapp; Owner: scapp
--

ALTER SEQUENCE worklog_actions_all_waa_id_seq OWNED BY worklog_actions_all.waa_id;


--
-- Name: worklog_files_all; Type: TABLE; Schema: scapp; Owner: scapp
--

CREATE TABLE worklog_files_all (
    wfa_id bigint NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    created_by character varying(30) NOT NULL,
    modified_at timestamp with time zone DEFAULT now() NOT NULL,
    modified_by character varying(30) NOT NULL,
    pwa_id bigint NOT NULL,
    wfa_name character varying(128) NOT NULL,
    wfa_mime_type character varying(128) NOT NULL,
    wfa_content_type character varying(128) NOT NULL,
    wfa_doc_size double precision NOT NULL,
    wfa_public boolean NOT NULL
);


ALTER TABLE worklog_files_all OWNER TO scapp;

--
-- Name: worklog_files_all_wfa_id_seq; Type: SEQUENCE; Schema: scapp; Owner: scapp
--

CREATE SEQUENCE worklog_files_all_wfa_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE worklog_files_all_wfa_id_seq OWNER TO scapp;

--
-- Name: worklog_files_all_wfa_id_seq; Type: SEQUENCE OWNED BY; Schema: scapp; Owner: scapp
--

ALTER SEQUENCE worklog_files_all_wfa_id_seq OWNED BY worklog_files_all.wfa_id;


--
-- Name: worklog_hours_all; Type: TABLE; Schema: scapp; Owner: scapp
--

CREATE TABLE worklog_hours_all (
    wha_id bigint NOT NULL,
    pwa_id bigint NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    created_by character varying(30) NOT NULL,
    modified_at timestamp with time zone DEFAULT now() NOT NULL,
    modified_by character varying(30) NOT NULL,
    wha_hours numeric(17,2) NOT NULL,
    wha_rate numeric(17,2) NOT NULL,
    wha_summary character varying(128) NOT NULL,
    wha_inv_date timestamp with time zone,
    wha_inv_number character varying(30)
);


ALTER TABLE worklog_hours_all OWNER TO scapp;

--
-- Name: worklog_hours_all_wha_id_seq; Type: SEQUENCE; Schema: scapp; Owner: scapp
--

CREATE SEQUENCE worklog_hours_all_wha_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE worklog_hours_all_wha_id_seq OWNER TO scapp;

--
-- Name: worklog_hours_all_wha_id_seq; Type: SEQUENCE OWNED BY; Schema: scapp; Owner: scapp
--

ALTER SEQUENCE worklog_hours_all_wha_id_seq OWNED BY worklog_hours_all.wha_id;


--
-- Name: cpa_id; Type: DEFAULT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY category_projects_all ALTER COLUMN cpa_id SET DEFAULT nextval('category_projects_all_cpa_id_seq'::regclass);


--
-- Name: cca_id; Type: DEFAULT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY client_categories_all ALTER COLUMN cca_id SET DEFAULT nextval('client_categories_all_cca_id_seq'::regclass);


--
-- Name: cpoa_id; Type: DEFAULT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY client_purchase_orders_all ALTER COLUMN cpoa_id SET DEFAULT nextval('client_purchase_orders_all_cpoa_id_seq'::regclass);


--
-- Name: cta_id; Type: DEFAULT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY client_teams_all ALTER COLUMN cta_id SET DEFAULT nextval('client_teams_all_cta_id_seq'::regclass);


--
-- Name: cua_id; Type: DEFAULT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY client_users_all ALTER COLUMN cua_id SET DEFAULT nextval('client_users_all_cua_id_seq'::regclass);


--
-- Name: pca_id; Type: DEFAULT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY portal_clients_all ALTER COLUMN pca_id SET DEFAULT nextval('portal_clients_all_pca_id_seq'::regclass);


--
-- Name: pa_id; Type: DEFAULT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY portals_all ALTER COLUMN pa_id SET DEFAULT nextval('portals_all_pa_id_seq'::regclass);


--
-- Name: pwa_id; Type: DEFAULT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY project_worklogs_all ALTER COLUMN pwa_id SET DEFAULT nextval('project_worklogs_all_pwa_id_seq'::regclass);


--
-- Name: tua_id; Type: DEFAULT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY team_users_all ALTER COLUMN tua_id SET DEFAULT nextval('team_users_all_tua_id_seq'::regclass);


--
-- Name: waa_id; Type: DEFAULT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY worklog_actions_all ALTER COLUMN waa_id SET DEFAULT nextval('worklog_actions_all_waa_id_seq'::regclass);


--
-- Name: wfa_id; Type: DEFAULT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY worklog_files_all ALTER COLUMN wfa_id SET DEFAULT nextval('worklog_files_all_wfa_id_seq'::regclass);


--
-- Name: wha_id; Type: DEFAULT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY worklog_hours_all ALTER COLUMN wha_id SET DEFAULT nextval('worklog_hours_all_wha_id_seq'::regclass);


--
-- Name: cca_pk; Type: CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY client_categories_all
    ADD CONSTRAINT cca_pk PRIMARY KEY (cca_id);


--
-- Name: cpa_pk; Type: CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY category_projects_all
    ADD CONSTRAINT cpa_pk PRIMARY KEY (cpa_id);


--
-- Name: cpoa_pk; Type: CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY client_purchase_orders_all
    ADD CONSTRAINT cpoa_pk PRIMARY KEY (cpoa_id);


--
-- Name: cta_pk; Type: CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY client_teams_all
    ADD CONSTRAINT cta_pk PRIMARY KEY (cta_id);


--
-- Name: cua_pk; Type: CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY client_users_all
    ADD CONSTRAINT cua_pk PRIMARY KEY (cua_id);


--
-- Name: pa_pk; Type: CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY portals_all
    ADD CONSTRAINT pa_pk PRIMARY KEY (pa_id);


--
-- Name: pca_pk; Type: CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY portal_clients_all
    ADD CONSTRAINT pca_pk PRIMARY KEY (pca_id);


--
-- Name: pwa_pk; Type: CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY project_worklogs_all
    ADD CONSTRAINT pwa_pk PRIMARY KEY (pwa_id);


--
-- Name: tua_pk; Type: CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY team_users_all
    ADD CONSTRAINT tua_pk PRIMARY KEY (tua_id);


--
-- Name: waa_pk; Type: CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY worklog_actions_all
    ADD CONSTRAINT waa_pk PRIMARY KEY (waa_id);


--
-- Name: wfa_pk; Type: CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY worklog_files_all
    ADD CONSTRAINT wfa_pk PRIMARY KEY (wfa_id);


--
-- Name: wha_pk; Type: CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY worklog_hours_all
    ADD CONSTRAINT wha_pk PRIMARY KEY (wha_id);


--
-- Name: cca_pca_fk_idx; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE INDEX cca_pca_fk_idx ON client_categories_all USING btree (pca_id);


--
-- Name: cca_uk1; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE UNIQUE INDEX cca_uk1 ON client_categories_all USING btree (pca_id, cca_code);


--
-- Name: cpa_cca_fk_idx; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE INDEX cpa_cca_fk_idx ON category_projects_all USING btree (cca_id);


--
-- Name: cpa_cpoa_fk_idx; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE INDEX cpa_cpoa_fk_idx ON category_projects_all USING btree (cpoa_id);


--
-- Name: cpa_tua_fk_idx; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE INDEX cpa_tua_fk_idx ON category_projects_all USING btree (tua_id);


--
-- Name: cpa_uk1; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE UNIQUE INDEX cpa_uk1 ON category_projects_all USING btree (cpa_title, cca_id);


--
-- Name: cpa_uk2; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE UNIQUE INDEX cpa_uk2 ON category_projects_all USING btree (cpa_url);


--
-- Name: cpa_uk3; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE UNIQUE INDEX cpa_uk3 ON category_projects_all USING btree (cpa_code, cca_id);


--
-- Name: cpoa_pca_fk_idx; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE INDEX cpoa_pca_fk_idx ON client_purchase_orders_all USING btree (pca_id);


--
-- Name: cpoa_uk1; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE UNIQUE INDEX cpoa_uk1 ON client_purchase_orders_all USING btree (pca_id, cpoa_number);


--
-- Name: cta_pca_fk_idx; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE INDEX cta_pca_fk_idx ON client_teams_all USING btree (pca_id);


--
-- Name: cta_uk1; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE UNIQUE INDEX cta_uk1 ON client_teams_all USING btree (pca_id, cta_code);


--
-- Name: cua_pca_fk_idx; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE INDEX cua_pca_fk_idx ON client_users_all USING btree (pca_id);


--
-- Name: cua_uk1; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE UNIQUE INDEX cua_uk1 ON client_users_all USING btree (pca_id, cua_email);


--
-- Name: pa_uk1; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE UNIQUE INDEX pa_uk1 ON portals_all USING btree (pa_code);


--
-- Name: pca_pa_fk_idx; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE INDEX pca_pa_fk_idx ON portal_clients_all USING btree (pa_id);


--
-- Name: pca_uk1; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE UNIQUE INDEX pca_uk1 ON portal_clients_all USING btree (pca_code, pa_id);


--
-- Name: pwa_cpa_fk_idx; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE INDEX pwa_cpa_fk_idx ON project_worklogs_all USING btree (cpa_id);


--
-- Name: tua_cta_fk_idx; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE INDEX tua_cta_fk_idx ON team_users_all USING btree (cta_id);


--
-- Name: tua_cua_fk_idx; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE INDEX tua_cua_fk_idx ON team_users_all USING btree (cua_id);


--
-- Name: tua_uk1; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE UNIQUE INDEX tua_uk1 ON team_users_all USING btree (cta_id, cua_id);


--
-- Name: waa_pwa_fk_idx; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE INDEX waa_pwa_fk_idx ON worklog_actions_all USING btree (pwa_id);


--
-- Name: wfa_pwa_fk_idx; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE INDEX wfa_pwa_fk_idx ON worklog_files_all USING btree (pwa_id);


--
-- Name: wfa_uk1; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE UNIQUE INDEX wfa_uk1 ON worklog_files_all USING btree (wfa_name);


--
-- Name: wha_pwa_fk_idx; Type: INDEX; Schema: scapp; Owner: scapp
--

CREATE INDEX wha_pwa_fk_idx ON worklog_hours_all USING btree (pwa_id);


--
-- Name: on_update_current_timestamp; Type: TRIGGER; Schema: scapp; Owner: scapp
--

CREATE TRIGGER on_update_current_timestamp BEFORE UPDATE ON category_projects_all FOR EACH ROW EXECUTE PROCEDURE on_update_current_timestamp_modified_at();


--
-- Name: on_update_current_timestamp; Type: TRIGGER; Schema: scapp; Owner: scapp
--

CREATE TRIGGER on_update_current_timestamp BEFORE UPDATE ON client_categories_all FOR EACH ROW EXECUTE PROCEDURE on_update_current_timestamp_modified_at();


--
-- Name: on_update_current_timestamp; Type: TRIGGER; Schema: scapp; Owner: scapp
--

CREATE TRIGGER on_update_current_timestamp BEFORE UPDATE ON client_purchase_orders_all FOR EACH ROW EXECUTE PROCEDURE on_update_current_timestamp_modified_at();


--
-- Name: on_update_current_timestamp; Type: TRIGGER; Schema: scapp; Owner: scapp
--

CREATE TRIGGER on_update_current_timestamp BEFORE UPDATE ON client_teams_all FOR EACH ROW EXECUTE PROCEDURE on_update_current_timestamp_modified_at();


--
-- Name: on_update_current_timestamp; Type: TRIGGER; Schema: scapp; Owner: scapp
--

CREATE TRIGGER on_update_current_timestamp BEFORE UPDATE ON client_users_all FOR EACH ROW EXECUTE PROCEDURE on_update_current_timestamp_modified_at();


--
-- Name: on_update_current_timestamp; Type: TRIGGER; Schema: scapp; Owner: scapp
--

CREATE TRIGGER on_update_current_timestamp BEFORE UPDATE ON portals_all FOR EACH ROW EXECUTE PROCEDURE on_update_current_timestamp_modified_at();


--
-- Name: on_update_current_timestamp; Type: TRIGGER; Schema: scapp; Owner: scapp
--

CREATE TRIGGER on_update_current_timestamp BEFORE UPDATE ON portal_clients_all FOR EACH ROW EXECUTE PROCEDURE on_update_current_timestamp_modified_at();


--
-- Name: on_update_current_timestamp; Type: TRIGGER; Schema: scapp; Owner: scapp
--

CREATE TRIGGER on_update_current_timestamp BEFORE UPDATE ON project_worklogs_all FOR EACH ROW EXECUTE PROCEDURE on_update_current_timestamp_modified_at();


--
-- Name: on_update_current_timestamp; Type: TRIGGER; Schema: scapp; Owner: scapp
--

CREATE TRIGGER on_update_current_timestamp BEFORE UPDATE ON team_users_all FOR EACH ROW EXECUTE PROCEDURE on_update_current_timestamp_modified_at();


--
-- Name: on_update_current_timestamp; Type: TRIGGER; Schema: scapp; Owner: scapp
--

CREATE TRIGGER on_update_current_timestamp BEFORE UPDATE ON worklog_actions_all FOR EACH ROW EXECUTE PROCEDURE on_update_current_timestamp_modified_at();


--
-- Name: on_update_current_timestamp; Type: TRIGGER; Schema: scapp; Owner: scapp
--

CREATE TRIGGER on_update_current_timestamp BEFORE UPDATE ON worklog_files_all FOR EACH ROW EXECUTE PROCEDURE on_update_current_timestamp_modified_at();


--
-- Name: on_update_current_timestamp; Type: TRIGGER; Schema: scapp; Owner: scapp
--

CREATE TRIGGER on_update_current_timestamp BEFORE UPDATE ON worklog_hours_all FOR EACH ROW EXECUTE PROCEDURE on_update_current_timestamp_modified_at();


--
-- Name: cca_pca_fk; Type: FK CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY client_categories_all
    ADD CONSTRAINT cca_pca_fk FOREIGN KEY (pca_id) REFERENCES portal_clients_all(pca_id);


--
-- Name: cpa_cca_fk; Type: FK CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY category_projects_all
    ADD CONSTRAINT cpa_cca_fk FOREIGN KEY (cca_id) REFERENCES client_categories_all(cca_id);


--
-- Name: cpa_cpoa_fk; Type: FK CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY category_projects_all
    ADD CONSTRAINT cpa_cpoa_fk FOREIGN KEY (cpoa_id) REFERENCES client_purchase_orders_all(cpoa_id);


--
-- Name: cpa_tua_fk; Type: FK CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY category_projects_all
    ADD CONSTRAINT cpa_tua_fk FOREIGN KEY (tua_id) REFERENCES team_users_all(tua_id);


--
-- Name: cpoa_pca_fk; Type: FK CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY client_purchase_orders_all
    ADD CONSTRAINT cpoa_pca_fk FOREIGN KEY (pca_id) REFERENCES portal_clients_all(pca_id);


--
-- Name: cta_pca_fk; Type: FK CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY client_teams_all
    ADD CONSTRAINT cta_pca_fk FOREIGN KEY (pca_id) REFERENCES portal_clients_all(pca_id);


--
-- Name: cua_pca_fk; Type: FK CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY client_users_all
    ADD CONSTRAINT cua_pca_fk FOREIGN KEY (pca_id) REFERENCES portal_clients_all(pca_id);


--
-- Name: pca_pa_fk; Type: FK CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY portal_clients_all
    ADD CONSTRAINT pca_pa_fk FOREIGN KEY (pa_id) REFERENCES portals_all(pa_id);


--
-- Name: pwa_cpa_fk; Type: FK CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY project_worklogs_all
    ADD CONSTRAINT pwa_cpa_fk FOREIGN KEY (cpa_id) REFERENCES category_projects_all(cpa_id);


--
-- Name: tua_cta_fk; Type: FK CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY team_users_all
    ADD CONSTRAINT tua_cta_fk FOREIGN KEY (cta_id) REFERENCES client_teams_all(cta_id);


--
-- Name: tua_cua_fk; Type: FK CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY team_users_all
    ADD CONSTRAINT tua_cua_fk FOREIGN KEY (cua_id) REFERENCES client_users_all(cua_id);


--
-- Name: waa_pwa_fk; Type: FK CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY worklog_actions_all
    ADD CONSTRAINT waa_pwa_fk FOREIGN KEY (pwa_id) REFERENCES project_worklogs_all(pwa_id);


--
-- Name: wfa_pwa_fk; Type: FK CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY worklog_files_all
    ADD CONSTRAINT wfa_pwa_fk FOREIGN KEY (pwa_id) REFERENCES project_worklogs_all(pwa_id);


--
-- Name: wha_pwa_fk; Type: FK CONSTRAINT; Schema: scapp; Owner: scapp
--

ALTER TABLE ONLY worklog_hours_all
    ADD CONSTRAINT wha_pwa_fk FOREIGN KEY (pwa_id) REFERENCES project_worklogs_all(pwa_id);


--
-- PostgreSQL database dump complete
--

