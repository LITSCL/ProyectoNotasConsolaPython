SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `dbproyectonotasconsolapython` DEFAULT CHARACTER SET utf8 ;
USE `dbproyectonotasconsolapython` ;

-- -----------------------------------------------------
-- Table `dbproyectonotasconsolapython`.`usuario`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `dbproyectonotasconsolapython`.`usuario` (
  `correo` VARCHAR(255) NOT NULL ,
  `nombre` VARCHAR(255) NULL DEFAULT NULL ,
  `apellido` VARCHAR(255) NULL DEFAULT NULL ,
  `clave` VARCHAR(255) NULL DEFAULT NULL ,
  `fecha` DATE NULL DEFAULT NULL ,
  PRIMARY KEY (`correo`) )
ENGINE = InnoDB
AUTO_INCREMENT = 17
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `dbproyectonotasconsolapython`.`nota`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `dbproyectonotasconsolapython`.`nota` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `titulo` VARCHAR(255) NULL DEFAULT NULL ,
  `descripcion` MEDIUMTEXT NULL DEFAULT NULL ,
  `fecha` DATE NULL DEFAULT NULL ,
  `usuario_correo` VARCHAR(255) NOT NULL ,
  PRIMARY KEY (`id`, `usuario_correo`) ,
  INDEX `fk_nota_usuario_idx` (`usuario_correo` ASC) ,
  CONSTRAINT `fk_nota_usuario`
    FOREIGN KEY (`usuario_correo` )
    REFERENCES `dbproyectonotasconsolapython`.`usuario` (`correo` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

USE `dbproyectonotasconsolapython` ;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
